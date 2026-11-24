# 医学证据与健康导航

[English](README.en.md) · [参考来源](SOURCES.md) · [临床覆盖](docs/clinical-coverage.md) · [同行调研](docs/comparison.md) · [发布下载](https://github.com/dingyucanada/medical-affairs-workflows/releases/latest)

从一次就诊前该准备什么，到一条医学主张由哪份证据支持，项目提供两项可分别安装的 Agent Skill。

| 你想做什么 | 选用的技能 |
| --- | --- |
| 找科室、准备就诊、看懂报告、了解预防保健、准备慢病复诊或罕见病第二意见 | [就医与健康导航](skills/medical-health-navigation/SKILL.md) · 面向公众、患者与照护者 · 预览版 |
| 查文献和试验、医学声称审查、制定医学计划、管理现场洞察、发表和药物警戒 | [医学事务与证据审查](skills/medical-affairs-workflows/SKILL.md) · 面向药企医学事务及生命科学团队 |

## 就医与健康导航

- **科室导航**覆盖 32 类常见就医和医技入口，从全科与儿科到心内、骨科、肿瘤、精神心理及遗传咨询。帮助核实医院科名并准备资料。 [科室索引](skills/medical-health-navigation/references/specialties.md)
- **看懂检查与诊断过程**解释术语、检查目的、报告原文和待确认的问题。急症先给就医行动。个体诊断和治疗安排由接诊团队评估。 [检查与诊断](skills/medical-health-navigation/references/tests-and-diagnosis.md)
- **保健、慢病与罕见病**提供按地区核对筛查或疫苗、常见慢病复诊、遗传报告和罕见病第二意见的路径。 [当前覆盖与边界](docs/clinical-coverage.md)

> 用 $medical-health-navigation 帮我读懂这段去掉个人信息的检查结论。分开写报告原话、需要医生确认的部分和复诊时要带的问题。

## 医学事务与证据审查

七个参考工作流覆盖检索、证据综合、医学计划、发表、洞察、沟通与药政。可用统一证据台账记录来源、声称、证据状态与编辑动作。中国及跨辖区监管核对记录正式出处、适用时点和缺项。 [64 项原目录映射](skills/medical-affairs-workflows/references/source-map.md) · [证据台账](skills/medical-affairs-workflows/references/ledger.md) · [监管来源](skills/medical-affairs-workflows/references/regulatory-sources.md)

> 用 $medical-affairs-workflows 审查这页医学交流材料。只核对给定摘要能支持的声称，逐条标出处、证据状态和修订动作。

## 安装与参与

从 [GitHub Releases](https://github.com/dingyucanada/medical-affairs-workflows/releases/latest) 下载想用的技能 ZIP。Codex 用户解压后把完整技能文件夹放入项目的 `.agents/skills/`，在新会话中用对应技能名调用。其他兼容客户端按其目录或 ZIP 导入流程安装。 [OpenAI 技能说明](https://learn.chatgpt.com/docs/build-skills)

欢迎用合成资料报告缺失科室、路由、参考来源和报告解释问题。新增病种内容需要明确适用人群、辖区、来源和临床复核状态。 [贡献指南](CONTRIBUTING.md) · [评测](evals/README.md) · [导航模拟验证](docs/navigation-validation.md) · [版本记录](CHANGELOG.md)

本项目的原创内容采用 Apache-2.0。第三方来源、授权和归属见来源索引。 [许可证](LICENSE) · [来源与归属](SOURCES.md)
