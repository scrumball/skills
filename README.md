# scrumball-skills

[中文说明](README.zh.md)

AI Skills package for influencer marketing operations across discovery, audience fit, realtime enrichment, campaign monitoring, and commerce intelligence.

> [!TIP]
> Best for teams that want AI to execute creator-data workflows via mapped `operationId` calls, not just generate text suggestions.

## ✨ What This Package Solves

- Turn natural-language campaign requests into executable skill workflows.
- Standardize creator evaluation across YouTube, TikTok, and Instagram.
- Make API capabilities transparent through per-skill operation indexes and request/response guides.

## 🚀 Quick Start

Install all skills:

```bash
npx skills add scrumball/skills
```

Install one skill only:

```bash
npx skills add scrumball/skills --skill <skill-name>
```

Run a quick local check (example):

```bash
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env list
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env call --operation ping
```

Expected result:
- `list` prints available `operationId`s.
- `call` returns JSON with `ok/status/data`.

## 🧭 Skill Selection Matrix

| Business goal | Skill | Platforms | Typical operationIds | Minimum identifiers |
|---|---|---|---|---|
| Build creator shortlist | `influencer-lead-discovery` | YouTube/TikTok/Instagram + cross-platform | `search_*`, `*_db_user_info`, `*_user_similar` | `query` keywords and platform account IDs |
| Evaluate audience alignment | `influencer-audience-fit-scoring` | YouTube/TikTok/Instagram | `audience_*` dimensions | `channel_id` / `unique_id` / `username` |
| Pull freshest profile/content signals | `influencer-realtime-enrichment` | YouTube/TikTok/Instagram | `*_realtime_user_*`, `*_realtime_video_detail` | platform user/video/media IDs |
| Operate and review campaign tracking | `influencer-campaign-monitoring` | YouTube/TikTok/Instagram + cross-platform | `create_monitor_task`, `list_monitor_tasks`, `*_monitor_metrics` | `monitor_id` or platform video/user IDs |
| Assess creator commerce potential | `influencer-commerce-intel` | TikTok-focused | `tiktok_user_shop_*`, `tiktok_realtime_product_detail` | `unique_id` / `product_id` |

## 📦 Included Skills

### `influencer-lead-discovery`
- Skill guide: [`skills/influencer-lead-discovery/SKILL.md`](skills/influencer-lead-discovery/SKILL.md)
- API index: [`skills/influencer-lead-discovery/references/api-index.md`](skills/influencer-lead-discovery/references/api-index.md)
- Request/response details: [`skills/influencer-lead-discovery/references/request-response.md`](skills/influencer-lead-discovery/references/request-response.md)

### `influencer-audience-fit-scoring`
- Skill guide: [`skills/influencer-audience-fit-scoring/SKILL.md`](skills/influencer-audience-fit-scoring/SKILL.md)
- API index: [`skills/influencer-audience-fit-scoring/references/api-index.md`](skills/influencer-audience-fit-scoring/references/api-index.md)
- Request/response details: [`skills/influencer-audience-fit-scoring/references/request-response.md`](skills/influencer-audience-fit-scoring/references/request-response.md)

### `influencer-realtime-enrichment`
- Skill guide: [`skills/influencer-realtime-enrichment/SKILL.md`](skills/influencer-realtime-enrichment/SKILL.md)
- API index: [`skills/influencer-realtime-enrichment/references/api-index.md`](skills/influencer-realtime-enrichment/references/api-index.md)
- Request/response details: [`skills/influencer-realtime-enrichment/references/request-response.md`](skills/influencer-realtime-enrichment/references/request-response.md)

### `influencer-campaign-monitoring`
- Skill guide: [`skills/influencer-campaign-monitoring/SKILL.md`](skills/influencer-campaign-monitoring/SKILL.md)
- API index: [`skills/influencer-campaign-monitoring/references/api-index.md`](skills/influencer-campaign-monitoring/references/api-index.md)
- Request/response details: [`skills/influencer-campaign-monitoring/references/request-response.md`](skills/influencer-campaign-monitoring/references/request-response.md)

### `influencer-commerce-intel`
- Skill guide: [`skills/influencer-commerce-intel/SKILL.md`](skills/influencer-commerce-intel/SKILL.md)
- API index: [`skills/influencer-commerce-intel/references/api-index.md`](skills/influencer-commerce-intel/references/api-index.md)
- Request/response details: [`skills/influencer-commerce-intel/references/request-response.md`](skills/influencer-commerce-intel/references/request-response.md)

## 💬 Prompt Patterns (with expected output)

- Discovery:
  - Prompt: "Find 20 TikTok sports creators in US/UK related to nike."
  - Output: ranked candidate table + selection rationale + risks + next step.

- Audience fit:
  - Prompt: "Score creator nike for US 18-24 basketball audience fit."
  - Output: numeric fit score + dimension breakdown + confidence + go/test/no-go.

- Monitoring:
  - Prompt: "List active monitor tasks and flag anomalies from last update."
  - Output: task status summary + anomaly list + optimization action.

## 🛠️ Troubleshooting

| Error | Likely cause | Fix |
|---|---|---|
| `SCRUMBALL_BASE_URL is required` | Missing gateway URL | Add `SCRUMBALL_BASE_URL` in `.env` and pass `--env-file .env` |
| `SCRUMBALL_API_KEY is required` | Missing API key | Add `SCRUMBALL_API_KEY` in `.env` |
| `Missing required ...` | Required query/body fields missing | Open the skill's `request-response.md` and provide required fields |
| `Unknown operationId` | Typo or wrong skill context | Run `... execute_operation.py ... list` to get valid operationIds |
| `Network error` / DNS failures | Temporary gateway/network issue | Retry, then check network/VPN/gateway status |
