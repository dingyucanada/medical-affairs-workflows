# Medical Affairs Workflows

[简体中文](README.md) · [Comparison](docs/comparison.md) · [Evaluation](evals/README.md) · [Changelog](CHANGELOG.md)

An Agent Skill for pharmaceutical Medical Affairs. One entry point routes requests to seven workflows covering retrieval, evidence review, medical planning, publication strategy, field insights, scientific communications, and drug safety and regulatory research.

## Use the skill

Download the skill ZIP from [GitHub Releases](https://github.com/dingyucanada/medical-affairs-workflows/releases). For Codex, extract the `medical-affairs-workflows` directory into your repository's `.agents/skills/` and invoke it as `$medical-affairs-workflows`. For other Agent Skills clients, use their skill directory or ZIP import workflow. The routing description is bilingual. Most detailed guides are in Simplified Chinese. Specify the language you need in your request.

> Use $medical-affairs-workflows to review the claims in this draft against the supplied abstract. Give the source location, evidence state, editorial action, and replacement language where needed.

[Skill entry point](skills/medical-affairs-workflows/SKILL.md) · [Original catalog mapping](skills/medical-affairs-workflows/references/source-map.md)

## What it produces

- A source-linked evidence review with separate evidence states and editorial actions. The optional, local JSON checker enforces structural consistency. [Evidence ledger](skills/medical-affairs-workflows/references/ledger.md)
- A China-focused regulatory audit with official entry points, dates, applicability, and gaps. The same process can show where other jurisdictions differ. [Regulatory source guide](skills/medical-affairs-workflows/references/regulatory-sources.md)
- Medical Affairs drafts at the depth and format requested. Source retrieval and authoring capabilities depend on the host. The optional checker uses only the Python 3 standard library.

Patient-specific treatment decisions, official submissions and approvals remain with the responsible clinical or organizational process. Use synthetic or public inputs when contributing examples.

Run [the checks and evaluations](evals/README.md) before contributing changes. The project uses [Apache-2.0](LICENSE) and ships [upstream attribution](skills/medical-affairs-workflows/NOTICE).
