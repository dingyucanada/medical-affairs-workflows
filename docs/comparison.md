# 同类项目调研与产品定位

调研日期为 2026-11-24。以下判断来自各项目自己的公开文档。测试、兼容性及能力范围按项目披露理解，未在本次调研中逐个部署实测。

| 项目 | 公开定位与可借鉴之处 |
| --- | --- |
| Open Medical Affairs AI | 英文、直接同行，也是本项目的上游来源。按医学事务任务拆分技能，提供合成工作坊、组织规则和公开数据入口。其任务拆分及人工决策点值得沿用。 [项目](https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills) |
| MedSci Skills | 英文为主并有中文文档。围绕医学研究、统计、期刊报告规范和投稿，公开介绍可重复的确定性检查。借鉴用小型机械检查解决可验证问题的做法。 [英文 README](https://github.com/Aperivue/medsci-skills) · [中文 README](https://github.com/Aperivue/medsci-skills/blob/main/README.zh-CN.md) |
| dyz-med-paper-skills | 面向中国医生和研究生的医学论文工作流，覆盖选题到修回。面向实际中文用户的提示、例子和操作解释值得借鉴。 [项目](https://github.com/duyunzhoudyz/dyz-med-paper-skills) |
| K-Dense Scientific Agent Skills | 英文通用科研工具库，公开列有临床研究和证据工作流。其按任务选择工具的方式适合更广科研环境。 [项目](https://github.com/K-Dense-AI/scientific-agent-skills) |
| aipoch Medical Research Skills | 医学科研技能目录，覆盖方案、分析、证据和写作，项目公开了审核框架。可借鉴把技能验证作为维护环节。 [项目](https://github.com/aipoch/medical-research-skills) |

## 由调研落到 v1.1

- **以药企医学事务交接为主线。** 采用一个入口和任务参考文件，覆盖医学策略、拜访与洞察、医学沟通、药物警戒和送审。中文为主，入口支持英文任务发现。
- **提供统一的证据台账。** 通过同一套字段，把来源获取状态、声称范围、当前证据状态、处理动作和替换文本放到可审阅的记录。可选的离线 Python 检查器要求已支持与已冲突有实际取得且定位的依据，对过强声称要求明确处置。
- **保留中国规则时点与跨辖区差异。** 增加官方来源入口、历史和现行规则、附件、触发日期与可复核的期限依据。保留「未判定」和人工追访的处理路径。
- **把失败行为写成可复跑用例。** 增加包含缺失、冲突、受限输入及非目标任务的合成用例，并持续分开记录格式检查、代码测试和模型行为验证。

以上是本项目的范围和实现选择。对外材料、企业 SOP 和真实系统运行仍需要适用环境里的验证。

## 开发规范

v1.0 的 `SKILL.md` 具备规范要求的命名、YAML 必填字段和 Markdown 正文，并以引用分层组织工作流。v1.1 增加规范推荐的参考校验器、版本化发布、双语发现、可重复的模型用例和针对离线检查器的回归测试。

[Agent Skills Specification](https://agentskills.io/specification) · [OpenAI Build Skills](https://learn.chatgpt.com/docs/build-skills) · [OpenAI 技能评测方法](https://developers.openai.com/blog/eval-skills)
