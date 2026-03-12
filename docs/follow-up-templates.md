# Missing-Parameter Follow-up Templates

Use these short prompts when the user goal is clear but the required identifier is missing.

## Core rule

- Ask only for the smallest missing identifier needed to execute the next API call.
- If multiple identifiers are accepted, ask for any one of them.
- Keep the follow-up specific to the platform and task.
- Treat task-map examples as documentation only unless `--use-example` is explicitly enabled.

## Copy-ready prompts

| Missing field | Ask the user |
|---|---|
| `query` | "What keyword, brand, or niche should I search for?" |
| `username` | "What Instagram username should I use?" |
| `unique_id` | "What TikTok unique_id or handle should I use?" |
| `channel_id` | "What YouTube `channel_id` should I use?" |
| `user_id` | "What `user_id` should I use?" |
| `uid` | "What platform `uid` should I use?" |
| `video_id` | "What `video_id` should I inspect?" |
| `media_code` | "What Instagram `media_code` should I inspect?" |
| `product_id` | "What TikTok `product_id` should I use?" |
| `monitor_id` | "What `monitor_id` should I use?" |
| `region` | "Which region code should I use, for example `US`?" |
| `video_code` | "What Instagram `video_code` should I use?" |

## Any-of templates

- `username` or `user_id`: "I can use either the username or the user_id. Which one do you have?"
- `unique_id` or `user_id`: "I can use either the TikTok handle (`unique_id`) or the `user_id`. Which one do you have?"
- `channel_id` or `username`: "I can use either the YouTube `channel_id` or the channel username. Which one do you have?"

## Task examples

- Lead discovery: "What keyword, brand, or niche should I search for on TikTok?"
- Audience fit: "What TikTok unique_id or handle should I score for audience fit?"
- Realtime enrichment: "What TikTok unique_id or user_id should I use for the realtime profile lookup?"
- Monitoring: "What `monitor_id` should I refresh?"
- Commerce: "What `product_id` and region code should I use for the TikTok product lookup?"

## Where to look next

- `docs/task-map.json`: machine-friendly task definitions plus per-task follow-up prompts
- `docs/task-map.md`: human-readable task starter matrix
- `scripts/scrumball_cli.py`: `demo --use-example` opt-in for intentional sample runs
- `skills/*/references/request-response.md`: exact required fields for each operation
