# Evidence ledger / 证据台账

多条医学声称、证据移交或送审时，可交付 Markdown 表或 UTF-8 JSON 台账。简短回答直接写证据与动作。若需要 JSON，按 [合成示例](../assets/synthetic-ledger.json) 组织，并在有 Python 3 的本地环境运行 `python3 scripts/check_ledger.py path/to/ledger.json`（从技能目录执行）。检查器仅读取文件，适合记录结构与一致性检查。

| 字段 | 约定 |
| --- | --- |
| `schema_version` | 整数 `1` |
| `sources[]` | `id`、`kind`、`access`、`reference`。可用类型为 `abstract`、`full_text`、`registry`、`regulatory_text`、`official_label`、`user_material`、`other`。 |
| `sources[].access` | `retrieved` 配实际取得日期 `accessed_on`（YYYY-MM-DD）。`unavailable` 或 `not_checked` 配 `reason`。摘要和无法取得的全文可各建一条。 |
| `claims[]` | `id`、`text`、`scope`、`status`、`reason`、`overstatement`（布尔值）、`action`、`evidence`。范围应写到对结论有意义的人群、比较组、地区、时点或数据层级。 |
| `status` | `supported` 已支持、`conflicting` 有冲突、`insufficient` 信息不足。将已打开的明确反证和无法取得区分开。 |
| `action` | `retain` 保留、`revise` 修订、`remove` 删除、`hold` 暂缓、`request_evidence` 补证。修订填 `replacement`。过强表述与已确认冲突应修订、删除或暂缓。 |
| `evidence[]` | 每项填 `source_id`、`relation`。决定性支持和反证使用 `supports`、`contradicts`，并填写已读的 `locator`，例如结果段、表格、附件或条款。相关背景使用 `context`。 |

书目元数据用于定位资料。具体数据或结论要指向实际读到的正文位置。保留一个来源在不同声称中的独立定位。附访问状态与当时看到的版本。对外引用原始报道时，分别核对是否忠实转述、自己的推断是否被支持。

检查器退出码 `0` 表示结构通过，`1` 表示台账结构或一致性有问题，`2` 表示文件或 JSON 无法读取。它不访问网络、验证引用真实性、判定证据质量或识别敏感信息。自行脱敏并在获准环境保存台账。
