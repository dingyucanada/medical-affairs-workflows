# 原目录与新工作流映射

来源是 2026 年 11 月 24 日核对的医学技能库目录。重构按任务归并工作规则，表中版本为原条目版本。对应位置指本包中的正文，许可证及原始署名见根目录 `NOTICE` 和 `upstream-notices/`。 [原始目录](https://medical-skills.pages.dev/skills) · [站点来源说明](https://medical-skills.pages.dev/about)

本包由一个入口和七个任务工作流组成。原站接口、连接器、渲染脚本、产品模板和计数机制属于各原条目的实现，本包采用宿主可用且获准的工具完成任务。表内链接可回查原文和原有配套文件。

## 文献检索与阅读

[打开整合工作流](retrieval.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [Placebo.PubMed 文献检索](https://medical-skills.pages.dev/skills/placebo-pubmed-search) | `placebo-pubmed-search` | 0.1.0 | 检索与更新 · PubMed |
| [Placebo.临床试验检索](https://medical-skills.pages.dev/skills/placebo-clinical-trials-search) | `placebo-clinical-trials-search` | 0.1.0 | 检索与更新 · 试验登记、状态、重复登记与项目归并 |
| [公开文献补充检索](https://medical-skills.pages.dev/skills/public-evidence-search) | `public-evidence-search` | 0.2.0 | 检索与更新 · 多库补查与溯源 |
| [文献与证据监测](https://medical-skills.pages.dev/skills/literature-surveillance) | `literature-surveillance` | 1.1.0 | 检索与更新 · 可复用监测基线和变化 |
| [读入已有文档](https://medical-skills.pages.dev/skills/document-ingestion) | `document-ingestion` | 1.0.0 | 读入、归档与术语 · 抽取范围、OCR、复核与安全扫描 |
| [表格整理](https://medical-skills.pages.dev/skills/spreadsheet-analysis) | `spreadsheet-analysis` | 1.0.0 | 读入、归档与术语 · 统计口径、去重和缺失 |
| [批准说明书与安全信息](https://medical-skills.pages.dev/skills/regulatory-label-intelligence) | `regulatory-label-intelligence` | 1.0.0 | 产品信息及引用核对 · 标签和公开安全资料 |
| [临床用语对照](https://medical-skills.pages.dev/skills/medical-terminology-mapping) | `medical-terminology-mapping` | 1.0.0 | 读入、归档与术语 · 术语映射与权限 |
| [引用核对](https://medical-skills.pages.dev/skills/citation-integrity) | `citation-integrity` | 1.1.0 | 产品信息及引用核对 · 来源与正文匹配 |
| [参考文献逐项核验](https://medical-skills.pages.dev/skills/nature-ref-verifier) | `nature-ref-verifier` | 1.0.1 | 产品信息及引用核对 · 书目逐字段核验 |

## 综述与证据综合

[打开整合工作流](evidence.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [临床证据评价](https://medical-skills.pages.dev/skills/evidence-appraisal) | `evidence-appraisal` | 1.0.0 | 单研究评价 · 设计、精确度、适用范围与偏倚 |
| [统计报告审查](https://medical-skills.pages.dev/skills/nature-statistics) | `nature-statistics` | 1.3.0 | 稿件与统计审查 · 分析单位、重复、误差和缺项 |
| [Placebo.医学证据与引用审查](https://medical-skills.pages.dev/skills/placebo-medical-evidence-citation-review) | `placebo-medical-evidence-citation-review` | 0.3.0 | 稿件与统计审查 · 证据状态与编辑动作 |
| [证据综合](https://medical-skills.pages.dev/skills/evidence-synthesis) | `evidence-synthesis` | 1.0.0 | 多项证据与研究缺口 · 按问题综合 |
| [系统文献综述](https://medical-skills.pages.dev/skills/systematic-literature-review) | `systematic-literature-review` | 1.0.0 | 多项证据与研究缺口 · 方案及可重复筛选 |
| [证据缺口](https://medical-skills.pages.dev/skills/evidence-gap-analysis) | `evidence-gap-analysis` | 1.0.0 | 多项证据与研究缺口 · 区分和优先排序 |

## 医学策略与医学计划

[打开整合工作流](strategy.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [医学计划](https://medical-skills.pages.dev/skills/medical-strategy-plan) | `medical-strategy-plan` | 1.0.0 | 从决策倒推工作 · 现状、优先事项与资源 |
| [策略取舍](https://medical-skills.pages.dev/skills/strategic-analysis) | `strategic-analysis` | 1.0.0 | 从决策倒推工作 · 备选方案、取舍和机会成本 |
| [整合证据计划](https://medical-skills.pages.dev/skills/integrated-evidence-plan) | `integrated-evidence-plan` | 1.0.0 | 从决策倒推工作 · 整合跨职能证据任务 |
| [医学工作成效](https://medical-skills.pages.dev/skills/medical-affairs-metrics) | `medical-affairs-metrics` | 1.0.0 | 从决策倒推工作 · 指标定义及归因界限 |
| [现场医学安排](https://medical-skills.pages.dev/skills/field-medical-planning) | `field-medical-planning` | 1.0.0 | 从决策倒推工作 · 区域覆盖、科学目标与容量 |
| [指南参与](https://medical-skills.pages.dev/skills/guideline-engagement) | `guideline-engagement` | 1.0.0 | 指南、顾问会与研究 · 指南时间与证据准备度 |
| [真实世界研究设计](https://medical-skills.pages.dev/skills/real-world-evidence-design) | `real-world-evidence-design` | 1.0.0 | 指南、顾问会与研究 · 目标试验设计和因果假设 |
| [研究者发起研究审阅](https://medical-skills.pages.dev/skills/investigator-initiated-study-review) | `investigator-initiated-study-review` | 1.0.0 | 指南、顾问会与研究 · 科学、支持和合规审阅 |
| [顾问会设计](https://medical-skills.pages.dev/skills/advisory-board-design) | `advisory-board-design` | 1.0.0 | 指南、顾问会与研究 · 顾问问题、会议设计与独立性 |
| [上市医学准备度](https://medical-skills.pages.dev/skills/launch-medical-readiness) | `launch-medical-readiness` | 1.1.0 | 上市医学工作 · 就绪与差距 |
| [上市时间与决策点](https://medical-skills.pages.dev/skills/launch-timeline-and-governance) | `launch-timeline-and-governance` | 1.0.0 | 上市医学工作 · 关键路径和决策点 |
| [上市医学计划](https://medical-skills.pages.dev/skills/medical-launch-plan) | `medical-launch-plan` | 1.0.0 | 上市医学工作 · 跨职能整合及阶段情景 |

## 发表规划

[打开整合工作流](publications.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [科学传播与发表规划](https://medical-skills.pages.dev/skills/scientific-communication-strategy) | `scientific-communication-strategy` | 1.0.0 | 科学传播与发表计划 · 受众、优先级、两类缺口 |
| [科学平台](https://medical-skills.pages.dev/skills/scientific-platform) | `scientific-platform` | 1.0.0 | 科学传播与发表计划 · 表述、证据和版本 |
| [科学文稿](https://medical-skills.pages.dev/skills/scientific-manuscript) | `scientific-manuscript` | 1.0.0 | 文稿和会议成果 · 投稿、报告规范与署名 |
| [大会摘要与壁报](https://medical-skills.pages.dev/skills/congress-abstract-and-poster) | `congress-abstract-and-poster` | 1.1.0 | 文稿和会议成果 · 大会要求和数据一致性 |
| [大会后解读](https://medical-skills.pages.dev/skills/congress-intelligence) | `congress-intelligence` | 1.0.0 | 文稿和会议成果 · 大会证据与判断变化 |

## 洞察挖掘

[打开整合工作流](insights.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [现场洞察综合](https://medical-skills.pages.dev/skills/field-insight-synthesis) | `field-insight-synthesis` | 1.0.0 | 从记录形成洞察 · 归并、分母、矛盾和责任 |
| [从记录形成洞察](https://medical-skills.pages.dev/skills/insight-generation) | `insight-generation` | 1.0.0 | 从记录形成洞察 · 观察转为决策依据 |
| [竞品科学动态](https://medical-skills.pages.dev/skills/competitive-intelligence) | `competitive-intelligence` | 1.0.0 | 竞品动态与专家互动 · 竞品证据更新 |
| [专家会面前准备](https://medical-skills.pages.dev/skills/kol-engagement-brief) | `kol-engagement-brief` | 1.0.0 | 竞品动态与专家互动 · 专家会面准备 |
| [拜访前准备](https://medical-skills.pages.dev/skills/msl-pre-call-planning) | `msl-pre-call-planning` | 0.2.0 | 竞品动态与专家互动 · 科学拜访前准备 |
| [拜访后整理](https://medical-skills.pages.dev/skills/msl-post-call-follow-up) | `msl-post-call-follow-up` | 0.2.0 | 竞品动态与专家互动 · 拜访事实、承诺及待办 |
| [现场事务整理](https://medical-skills.pages.dev/skills/msl-administrative-operations) | `msl-administrative-operations` | 0.2.0 | 竞品动态与专家互动 · 事务及覆盖状态 |
| [寻找相关专业人士](https://medical-skills.pages.dev/skills/hcp-discovery-and-access) | `hcp-discovery-and-access` | 0.2.0 | 竞品动态与专家互动 · 专业人士发现与机构渠道 |
| [读取已有数据](https://medical-skills.pages.dev/skills/data-connection) | `data-connection` | 0.2.0 | 竞品动态与专家互动 · 授权导出或只读查询 |

## 医学沟通与演示

[打开整合工作流](communications.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [非推广医学幻灯](https://medical-skills.pages.dev/skills/medical-slide-deck) | `medical-slide-deck` | 1.1.0 | 幻灯、图文与通俗版本 · 非推广幻灯 |
| [通俗语言摘要](https://medical-skills.pages.dev/skills/plain-language-summary) | `plain-language-summary` | 1.0.0 | 幻灯、图文与通俗版本 · 患者及公众摘要 |
| [可视化摘要](https://medical-skills.pages.dev/skills/visual-abstract) | `visual-abstract` | 1.1.0 | 幻灯、图文与通俗版本 · 图解研究 |
| [临床数据图](https://medical-skills.pages.dev/skills/data-visualization-for-medical) | `data-visualization-for-medical` | 1.1.0 | 幻灯、图文与通俗版本 · 临床数据图 |
| [医学示意图](https://medical-skills.pages.dev/skills/diagram-and-schema) | `diagram-and-schema` | 1.1.0 | 幻灯、图文与通俗版本 · 流程、机制和证据示意 |
| [给管理层的简报](https://medical-skills.pages.dev/skills/executive-briefing) | `executive-briefing` | 1.0.0 | 对象、场合和内容运维 · 决策简报 |
| [医学问询回复](https://medical-skills.pages.dev/skills/medical-information-response) | `medical-information-response` | 1.1.0 | 对象、场合和内容运维 · 医学问询与标准答复 |
| [医学信函](https://medical-skills.pages.dev/skills/medical-correspondence) | `medical-correspondence` | 1.0.0 | 对象、场合和内容运维 · 对外草拟信函 |
| [医学教育安排](https://medical-skills.pages.dev/skills/medical-education-program) | `medical-education-program` | 1.0.0 | 对象、场合和内容运维 · 教育目标与组织责任 |
| [安全性沟通](https://medical-skills.pages.dev/skills/safety-communication) | `safety-communication` | 1.0.0 | 对象、场合和内容运维 · 安全性沟通 |
| [患者参与安排](https://medical-skills.pages.dev/skills/patient-engagement-planning) | `patient-engagement-planning` | 0.2.0 | 对象、场合和内容运维 · 患者参与和反馈闭环 |
| [会议记录整理](https://medical-skills.pages.dev/skills/meeting-transcription) | `meeting-transcription` | 0.2.0 | 对象、场合和内容运维 · 录音、转写与会后事项 |
| [现场上市培训](https://medical-skills.pages.dev/skills/launch-field-training) | `launch-field-training` | 1.0.0 | 对象、场合和内容运维 · 上市培训和边界演练 |
| [医学内容维护](https://medical-skills.pages.dev/skills/medical-content-operations) | `medical-content-operations` | 0.2.0 | 对象、场合和内容运维 · 内容版本和维护 |
| [支付与评估材料](https://medical-skills.pages.dev/skills/payer-value-dossier) | `payer-value-dossier` | 1.0.0 | 对象、场合和内容运维 · 支付评估和预算影响 |
| [推广材料的医学核对](https://medical-skills.pages.dev/skills/promotional-material-medical-review) | `promotional-material-medical-review` | 1.1.0 | 送审和成稿复核 · 推广材料医学核查 |
| [送审前检查](https://medical-skills.pages.dev/skills/mlr-review-readiness) | `mlr-review-readiness` | 1.0.0 | 送审和成稿复核 · 医学、法律和注册送审准备 |
| [成稿自查](https://medical-skills.pages.dev/skills/deliverable-quality-review) | `deliverable-quality-review` | 1.0.0 | 送审和成稿复核 · 数字、引用与交付核对 |

## 药物安全、药物警戒与药政检索

[打开整合工作流](safety-regulatory.md)

| 原始条目 | 原 ID | 原版本 | 整合位置及重点 |
| --- | --- | --- | --- |
| [Placebo.药品注册要求检索](https://medical-skills.pages.dev/skills/placebo-china-drug-registration) | `placebo-china-drug-registration` | 0.1.0 | 中国药品注册要求 · 分类、时点、过渡和期限 |
| [Placebo.药物警戒要求检索](https://medical-skills.pages.dev/skills/placebo-china-pharmacovigilance) | `placebo-china-pharmacovigilance` | 0.1.0 | 中国药物警戒义务 · 主体、附件、要素及升级 |
| [Placebo.安全信号研究设计](https://medical-skills.pages.dev/skills/placebo-safety-signal-study-design) | `placebo-safety-signal-study-design` | 0.1.0 | 安全信号与研究设计 · 检测、验证、风险量化 |
| [Placebo.不良反应病例叙事](https://medical-skills.pages.dev/skills/placebo-china-icsr-narrative) | `placebo-china-icsr-narrative` | 0.1.0 | 个例叙事 · 事实、相对时间与五项判断 |
