# Third-Party Notices

Version 0.3.0 does not ship the 0.1.0 reference or script files as runtime dependencies, but it remains a derivative of the same upstream works, so the notices below still apply.

This prototype is licensed under Apache-2.0 (see `LICENSE`). This file records
third-party work that is incorporated, summarised, or architecturally relevant,
and the terms that apply. It does not change the Apache License.

The full Open Medical Affairs AI third-party notice, including sections that
apply to skills not shipped here, is preserved at
`provenance/licenses/oma-THIRD-PARTY-NOTICES.md`. The excerpt below is the
part that pertains to files used in this prototype.

---

## 1. K-Dense-AI/scientific-agent-skills — MIT License

**Source:** https://github.com/K-Dense-AI/scientific-agent-skills
**License:** MIT
**Copyright:** Copyright (c) K-Dense Inc.

Open Medical Affairs AI recorded that it did **not** copy files from that
project. It studied the architecture of certain MIT-licensed skills and
rewrote that architecture for Medical Affairs. For the skills used here, the
upstream notice states that `skills/citation-integrity/` is architecturally
derived from the pattern of multi-source metadata reconciliation
(CrossRef / PubMed / OpenAlex) and verification-before-formatting ordering
in K-Dense `citation-management`.

This prototype likewise does not copy K-Dense files. Because it includes
substantial portions of `citation-integrity`, the same architectural
attribution is carried forward.

The MIT license text, as reproduced in the upstream notice:

```
MIT License

Copyright (c) K-Dense Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

The upstream notice also warns that some other files inside the K-Dense
repository (docx/pptx skills) are proprietary Anthropic skills and are not
MIT licensed. Those files were not used by Open Medical Affairs AI and are
not used here.

---

## 2. Journal instructions and official instruments — not Apache works of this package

The following are not licensed as Apache-2.0 works of 医学技能库, Open
Medical Affairs AI, or nature-skills, even when a local summary or working
checklist is shipped for offline review:

- Nature, Nature Portfolio, and Nature Machine Intelligence author
  instructions and reporting summaries. Local files such as
  `references/nature-article-requirements.md`,
  `references/upstream-nmi-format.md`, and parts of
  `references/source-basis.md` are study aids. Re-open the current journal
  page before stating what a journal requires.
- Reporting guidelines issued by their owners (CONSORT, STROBE, PRISMA,
  ARRIVE and similar). This package does not ship those guideline texts.
- Risk-of-bias and certainty frameworks described in
  `references/bias-checklists.md` and `references/grade.md` (RoB 2, ROBINS-I,
  Newcastle-Ottawa, QUADAS-2, GRADE). The files are working notes from the
  Open Medical Affairs AI skill, not official instrument redistributions.
  Use the current official guidance when a formal assessment must be filed.

---

## 3. Public data sources queried at runtime (not redistributed)

No records from these sources are shipped in this directory. If a module
queries them live, their own terms and rate limits apply:

- NCBI E-utilities (PubMed / PMC)
- Crossref REST API
- OpenAlex (CC0 metadata)
- ClinicalTrials.gov API v2
- Publisher or journal public landing pages reached via doi.org

This prototype does not assume a login to CNKI, Wanfang, Zotero, or any
subscription database, and it does not ship MedDRA, SNOMED CT, ICD, or WHO
Drug Dictionary content.
