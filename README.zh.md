# scrumball-skills

[English](README.md)

面向网红营销场景的 AI Skills 套件，覆盖达人发现、受众匹配、实时补数、投放监控和电商分析。

> [!TIP]
> 适合希望 AI 直接调用 `operationId` 执行数据工作流，而不仅是生成建议文本的团队。

## ✨ 解决什么问题

- 把自然语言营销需求转成可执行的 skill 调用链路。
- 在 YouTube / TikTok / Instagram 上统一达人评估流程。
- 通过每个 skill 的 API 索引和请求/返回文档，提升接口透明度。

## 🚀 快速开始

安装全部 skills：

```bash
npx skills add scrumball/skills
```

只安装一个 skill：

```bash
npx skills add scrumball/skills --skill <skill-name>
```

本地快速验证（示例）：

```bash
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env list
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env call --operation ping
```

预期结果：
- `list` 会输出可用 `operationId` 列表。
- `call` 会返回包含 `ok/status/data` 的 JSON。

## 🧭 Skill 选择矩阵

| 业务目标 | Skill | 平台 | 常用 operationId | 最小标识字段 |
|---|---|---|---|---|
| 建立达人候选池 | `influencer-lead-discovery` | YouTube/TikTok/Instagram + 跨平台 | `search_*`, `*_db_user_info`, `*_user_similar` | `query` 关键词 + 平台账号标识 |
| 评估受众匹配度 | `influencer-audience-fit-scoring` | YouTube/TikTok/Instagram | `audience_*` 维度接口 | `channel_id` / `unique_id` / `username` |
| 拉取最新账号/内容信号 | `influencer-realtime-enrichment` | YouTube/TikTok/Instagram | `*_realtime_user_*`, `*_realtime_video_detail` | 平台 user/video/media ID |
| 执行和复盘监控任务 | `influencer-campaign-monitoring` | YouTube/TikTok/Instagram + 跨平台 | `create_monitor_task`, `list_monitor_tasks`, `*_monitor_metrics` | `monitor_id` 或平台 video/user ID |
| 评估达人电商变现能力 | `influencer-commerce-intel` | TikTok 为主 | `tiktok_user_shop_*`, `tiktok_realtime_product_detail` | `unique_id` / `product_id` |

## 📦 包含的 Skills

### `influencer-lead-discovery`
- 文档：[`skills/influencer-lead-discovery/SKILL.md`](skills/influencer-lead-discovery/SKILL.md)
- API 索引：[`skills/influencer-lead-discovery/references/api-index.md`](skills/influencer-lead-discovery/references/api-index.md)
- 请求/返回：[`skills/influencer-lead-discovery/references/request-response.md`](skills/influencer-lead-discovery/references/request-response.md)

### `influencer-audience-fit-scoring`
- 文档：[`skills/influencer-audience-fit-scoring/SKILL.md`](skills/influencer-audience-fit-scoring/SKILL.md)
- API 索引：[`skills/influencer-audience-fit-scoring/references/api-index.md`](skills/influencer-audience-fit-scoring/references/api-index.md)
- 请求/返回：[`skills/influencer-audience-fit-scoring/references/request-response.md`](skills/influencer-audience-fit-scoring/references/request-response.md)

### `influencer-realtime-enrichment`
- 文档：[`skills/influencer-realtime-enrichment/SKILL.md`](skills/influencer-realtime-enrichment/SKILL.md)
- API 索引：[`skills/influencer-realtime-enrichment/references/api-index.md`](skills/influencer-realtime-enrichment/references/api-index.md)
- 请求/返回：[`skills/influencer-realtime-enrichment/references/request-response.md`](skills/influencer-realtime-enrichment/references/request-response.md)

### `influencer-campaign-monitoring`
- 文档：[`skills/influencer-campaign-monitoring/SKILL.md`](skills/influencer-campaign-monitoring/SKILL.md)
- API 索引：[`skills/influencer-campaign-monitoring/references/api-index.md`](skills/influencer-campaign-monitoring/references/api-index.md)
- 请求/返回：[`skills/influencer-campaign-monitoring/references/request-response.md`](skills/influencer-campaign-monitoring/references/request-response.md)

### `influencer-commerce-intel`
- 文档：[`skills/influencer-commerce-intel/SKILL.md`](skills/influencer-commerce-intel/SKILL.md)
- API 索引：[`skills/influencer-commerce-intel/references/api-index.md`](skills/influencer-commerce-intel/references/api-index.md)
- 请求/返回：[`skills/influencer-commerce-intel/references/request-response.md`](skills/influencer-commerce-intel/references/request-response.md)

## 💬 Prompt 示例（含预期输出）

- 达人发现：
  - Prompt: “找 20 个与 nike 相关、面向美英市场的 TikTok 体育达人。”
  - 输出：候选人排序表 + 选择理由 + 风险 + 下一步动作。

- 受众匹配：
  - Prompt: “评估达人 nike 对美国 18-24 岁篮球人群的匹配度。”
  - 输出：匹配分 + 维度拆解 + 置信度 + go/test/no-go 结论。

- 监控复盘：
  - Prompt: “列出活跃监控任务，并标出上次更新后的异常。”
  - 输出：任务状态汇总 + 异常清单 + 优化建议。

## 🛠️ 常见报错排查

| 报错 | 可能原因 | 处理方式 |
|---|---|---|
| `SCRUMBALL_BASE_URL is required` | 网关地址缺失 | 在 `.env` 中补充 `SCRUMBALL_BASE_URL`，并使用 `--env-file .env` |
| `SCRUMBALL_API_KEY is required` | API Key 缺失 | 在 `.env` 中补充 `SCRUMBALL_API_KEY` |
| `Missing required ...` | 缺少必填 query/body 字段 | 打开对应 skill 的 `request-response.md` 按必填字段补齐 |
| `Unknown operationId` | operationId 拼写错误或 skill 用错 | 执行 `... execute_operation.py ... list` 获取合法 operationId |
| `Network error` / DNS 错误 | 临时网络或网关不可达 | 重试后检查网络/VPN/网关状态 |
