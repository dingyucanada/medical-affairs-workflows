#!/usr/bin/env python3
"""Check the local evidence ledger for structural inconsistencies."""

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys


SOURCE_KINDS = {
    "abstract", "full_text", "registry", "regulatory_text", "official_label",
    "user_material", "other",
}
ACCESS = {"retrieved", "unavailable", "not_checked"}
STATES = {"supported", "conflicting", "insufficient"}
ACTIONS = {"retain", "revise", "remove", "hold", "request_evidence"}
RELATIONS = {"supports", "contradicts", "context"}
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}")
ISO_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


def is_date(value):
    if not isinstance(value, str) or ISO_DATE.fullmatch(value) is None:
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def is_text(value):
    return isinstance(value, str) and bool(value.strip())


def is_choice(value, allowed):
    return isinstance(value, str) and value in allowed


def validate(ledger):
    errors = []

    def check(condition, field, message):
        if not condition:
            errors.append(f"{field}: {message}")
        return condition

    def entries(key):
        items = ledger.get(key)
        if check(isinstance(items, list), key, "must be an array"):
            return items
        return []

    def unique_id(record, field, known):
        identifier = record.get("id")
        valid = isinstance(identifier, str) and IDENTIFIER.fullmatch(identifier)
        if not check(valid, f"{field}.id", "must be a nonempty ASCII identifier"):
            return None
        if not check(identifier not in known, f"{field}.id", "duplicates an earlier id"):
            return None
        known.add(identifier)
        return identifier

    if not isinstance(ledger, dict):
        return ["ledger: must be an object"]
    version = ledger.get("schema_version")
    check(type(version) is int and version == 1, "schema_version", "must be 1")
    source_ids = set()
    sources = {}

    for index, source in enumerate(entries("sources")):
        field = f"sources[{index}]"
        if not check(isinstance(source, dict), field, "must be an object"):
            continue
        identifier = unique_id(source, field, source_ids)
        access = source.get("access")
        kind = source.get("kind")
        check(is_choice(access, ACCESS), f"{field}.access", "unknown access state")
        check(is_choice(kind, SOURCE_KINDS), f"{field}.kind", "unknown source kind")
        check(is_text(source.get("reference")), f"{field}.reference", "needs a resolvable or local reference")
        if access == "retrieved":
            check(is_date(source.get("accessed_on")), f"{field}.accessed_on", "needs a real YYYY-MM-DD date")
        if access in ("unavailable", "not_checked"):
            check(is_text(source.get("reason")), f"{field}.reason", "explain the gap")
        if identifier is not None:
            sources[identifier] = source

    claims = entries("claims")
    check(bool(claims), "claims", "needs at least one claim")
    claim_ids = set()
    for index, claim in enumerate(claims):
        field = f"claims[{index}]"
        if not check(isinstance(claim, dict), field, "must be an object"):
            continue
        unique_id(claim, field, claim_ids)
        for key in ("text", "scope", "reason"):
            check(is_text(claim.get(key)), f"{field}.{key}", "must be nonempty text")
        status = claim.get("status")
        action = claim.get("action")
        overstatement = claim.get("overstatement")
        check(is_choice(status, STATES), f"{field}.status", "unknown evidence state")
        check(is_choice(action, ACTIONS), f"{field}.action", "unknown action")
        check(type(overstatement) is bool, f"{field}.overstatement", "must be a Boolean")
        if action == "revise":
            check(is_text(claim.get("replacement")), f"{field}.replacement", "required for revision")
        if overstatement is True or status == "conflicting":
            check(action in ("revise", "remove", "hold"), f"{field}.action", "an overstatement or conflict must be revised, removed, or held")
        evidence = claim.get("evidence")
        if not check(isinstance(evidence, list), f"{field}.evidence", "must be an array"):
            continue
        decisive = set()
        for e_index, item in enumerate(evidence):
            pointer = f"{field}.evidence[{e_index}]"
            if not check(isinstance(item, dict), pointer, "must be an object"):
                continue
            source_id = item.get("source_id")
            source = sources.get(source_id) if isinstance(source_id, str) else None
            check(source is not None, f"{pointer}.source_id", "unknown source id")
            relation = item.get("relation")
            check(is_choice(relation, RELATIONS), f"{pointer}.relation", "unknown evidence relation")
            if relation in ("supports", "contradicts"):
                located = check(is_text(item.get("locator")), f"{pointer}.locator", "required for decisive evidence")
                readable = check(source is not None and source.get("access") == "retrieved",
                                 f"{pointer}.source_id", "decisive evidence must be retrieved")
                if located and readable:
                    decisive.add(relation)
        if status == "supported":
            check("supports" in decisive and "contradicts" not in decisive, f"{field}.status",
                  "supported requires located support and no unresolved decisive contradiction")
        if status == "conflicting":
            check("contradicts" in decisive, f"{field}.status", "conflicting requires a located contradiction")
    return errors


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("JSON contains a duplicate field")
        result[key] = value
    return result


def reject_nonfinite(_value):
    raise ValueError("JSON contains a non-finite number")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path)
    args = parser.parse_args()
    try:
        with args.ledger.open(encoding="utf-8") as stream:
            ledger = json.load(stream, object_pairs_hook=reject_duplicate_keys,
                               parse_constant=reject_nonfinite)
    except (OSError, ValueError) as error:
        print(f"Could not read ledger ({type(error).__name__}).", file=sys.stderr)
        return 2
    errors = validate(ledger)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Ledger structure passed. Source truth and medical judgment still require review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
