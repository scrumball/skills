---
name: influencer-campaign-monitoring
description: Campaign monitoring and review operations. Use when users ask to create/list/detail/refresh/stop monitoring tasks, retrieve creator monitoring metrics during campaign execution, download tracked assets, or build post-campaign performance reviews.
---

# Influencer Campaign Monitoring

Operate monitoring tasks and convert tracking data into review insights.

## Quick Start

1. Identify monitoring scope (platform, creator/video, timeframe).
2. Create or retrieve monitoring tasks.
3. Pull metrics and task status repeatedly.
4. Summarize trend, anomalies, and actions.

## Workflow

1. Task lifecycle:
- Create task (`create_monitor_task`)
- List/detail tasks (`list_monitor_tasks`, `get_monitor_task_detail`)
- Refresh or stop as needed

2. Metric retrieval:
- Pull user monitor metrics per platform.
- Download relevant video assets when needed for review.

3. Review output:
- Track progress vs expected outcome.
- Highlight anomalies and suggested interventions.

## Tooling

Execution commands:
- List operations: `python3 scripts/execute_operation.py --env-file .env list`
- Create task: `python3 scripts/execute_operation.py --env-file .env call --operation create_monitor_task --body '{"platform":"tiktok","video_id":"123456"}'`
- List tasks: `python3 scripts/execute_operation.py --env-file .env call --operation list_monitor_tasks --query '{"page":1,"page_size":20}'`


Required environment variables:
- `SCRUMBALL_BASE_URL`: API gateway base URL
- `SCRUMBALL_API_KEY`: unified API key
- Optional: `SCRUMBALL_AUTH_PREFIX`, `SCRUMBALL_TIMEOUT_SECONDS`

Env loading:
- Use `--env-file .env` for explicit loading.
- Without `--env-file`, script auto-tries `./.env` then `<skill-root>/.env`.

## Output Contract

Always return:
- `Task status`: active/completed/stopped + identifiers
- `Performance trend`: key metric movement
- `Anomalies`: unexpected spikes/drops
- `Recommendation`: continue, adjust, or stop

## Failure Handling

- If task creation fails, validate platform and video identifier first.
- If metric endpoints lag, report delayed freshness explicitly.
- If user requests audience fit conclusions, hand off to audience-fit skill.

## References

- `references/api-index.md`
- `references/request-response.md`
- `references/operations.json`
