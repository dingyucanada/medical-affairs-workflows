# Third-Party Notices

本离线原型按 Apache-2.0 提供（见 LICENSE）。本文件记录对照或方法上来自第三方的作品，以及适用的条款。它不改变 Apache 许可证。

## 1. Open Medical Affairs AI — pubmed-search、clinical-trials-search、public-evidence-search

**来源：** https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills
**固定提交：** 006762f50e1ea28580e2965483a2b08a99253284
**许可：** Apache License, Version 2.0
**著作权声明：** Copyright 2026 Open Medical Affairs AI and contributors

本重写稿在功能上承接「PubMed 文献检索」，并在对照「临床试验检索」「公开文献补充检索」时吸收了可复核检索、库边界和取证失败不得编造等方法。本包没有复制这些技能的正文、参考文件或脚本，检索时也不加载它们。完整上游 LICENSE 和 NOTICE 见 `provenance/licenses/oma-LICENSE`、`provenance/licenses/oma-NOTICE`。

该上游 NOTICE 还说明：项目产出供有资质的人审阅的草稿，不是医疗器械、临床决策支持或监管系统中的正式记录。它同时记录，其仓库中部分其他技能在架构上参考过 K-Dense Inc. 的 MIT 许可技能（https://github.com/K-Dense-AI/scientific-agent-skills）。「PubMed 文献检索」不在那张对照表中，本包也没有复制或改写 K-Dense 的文件。

## 2. NCBI、PubMed 与公开词表 — 不是本包的 Apache 作品

下列文本、记录和接口即使在说明里被列为检索起点或既往核对记录，也不是安未稷、本包或对照技能的 Apache 作品：

- NCBI E-utilities 接口及其官方说明
- PubMed / MEDLINE 书目记录，以及 PubMed Central 中可公开取得的全文
- 医学主题词（MeSH）词表
- ClinicalTrials.gov、Europe PMC、Crossref 等对照技能提到的其他公开数据源

使用时须重新打开各来源当日有效的说明和使用政策。本包不重新分发这些记录，也不把 Open Medical Affairs AI 或 NCBI 写成这些原文的著作权人。
