# 医学事务工作流

[English](README.en.md) · [同类调研](docs/comparison.md) · [评测](evals/README.md) · [版本记录](CHANGELOG.md)

面向药企医学事务团队的 Agent Skill。它把文献与试验、医学声称审查、策略和上市、现场洞察、发表沟通、药物警戒及中国药政连接成七个工作流。一个入口按任务选择参考文件，交付可复核的来源、局限和下一步。

## 使用

在 [GitHub Releases](https://github.com/dingyucanada/medical-affairs-workflows/releases) 下载技能 ZIP 并解压。Codex 用户可将整个 `medical-affairs-workflows` 文件夹放入自己项目的 `.agents/skills/`。支持技能 ZIP 导入的客户端可使用发布资产。启动新会话后可明确调用 `$medical-affairs-workflows`。支持通用 Agent Skills 的其他客户端按其技能目录说明安装。

> 用 $medical-affairs-workflows 审查这页医学交流材料。只核对给定摘要能支持的声称，逐条标出处、证据状态和修订建议。

[技能入口](skills/medical-affairs-workflows/SKILL.md) · [64 条上游能力映射](skills/medical-affairs-workflows/references/source-map.md) · [官方技能安装说明](https://learn.chatgpt.com/docs/build-skills)

## 核心设计

- **证据台账**同时记录读到的来源、声称范围、证据状态和编辑动作。跨团队移交时可提供 JSON。离线检查器可找出采用未取得来源作为决定性依据、过强声称没有处置、缺少定位等结构错误。 [字段说明](skills/medical-affairs-workflows/references/ledger.md)
- **中国监管时点核查**明确辖区、主体、产品、日期、原文和附件，分别记录已取得原文、缺失或冲突，以及应由负责人复核的事项。 [官方来源与时点](skills/medical-affairs-workflows/references/regulatory-sources.md)
- **按任务交付**支持简短对话、结构化台账或指定格式的材料。核心流程不绑定渲染器，离线检查器使用 Python 3 标准库。外部检索和文件生成取决于宿主环境。

适用场景为检索、起草和专业复核。涉及个体治疗、监管提交或正式批准时，由适用的临床或企业流程负责。贡献示例请使用合成或可公开的材料。

## 本地验证

```sh
skills-ref validate skills/medical-affairs-workflows
python3 tools/check_links.py
python3 -m unittest discover -s tests -v
python3 tools/package_skill.py
```

[Agent Skills 参考校验器](https://github.com/agentskills/agentskills/tree/main/skills-ref)检查技能格式。[评测](evals/README.md)记录可供复跑的合成案例。格式、软件测试、模型行为和生产验证分别记录。

本项目采用 Apache-2.0。上游版权、许可证和第三方归属随技能包提供。 [许可证](LICENSE) · [来源和改动](skills/medical-affairs-workflows/NOTICE)
