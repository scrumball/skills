---
name: influencer-realtime-enrichment
description: Realtime data enrichment for creators and content. Use when users ask for up-to-date creator/content status, latest post or video details, realtime profile changes, or freshness-critical checks during active campaigns.
---

# Influencer Realtime Enrichment

Fetch fresh creator and content data when snapshot data is not enough.

## Quick Start

1. Confirm urgency and freshness expectation.
2. Choose platform and object type (user/media/video/story).
3. Call realtime endpoints from `references/api-index.md`.
4. Compare against baseline assumptions and summarize deltas.

## Workflow

1. Define enrichment target:
- Creator-level: profile, recent posts/videos
- Content-level: media/video detail

2. Execute realtime retrieval:
- Prioritize detail endpoints for decision-critical objects.
- Use paginated pulls for recent content sets.

3. Produce delta-oriented output:
- Report what changed, not only raw payload.
- Flag sudden spikes/drops and potential campaign impact.

## Tooling

Execution commands:
- List operations: `python3 scripts/execute_operation.py --env-file .env list`
- Example user enrichment: `python3 scripts/execute_operation.py --env-file .env call --operation tiktok_realtime_user_info --query '{"unique_id":"nike"}'`
- Example content enrichment: `python3 scripts/execute_operation.py --env-file .env call --operation youtube_realtime_video_detail --query '{"video_id":"dQw4w9WgXcQ"}'`


Required environment variables:
- `SCRUMBALL_BASE_URL`: API gateway base URL
- `SCRUMBALL_API_KEY`: unified API key
- Optional: `SCRUMBALL_AUTH_PREFIX`, `SCRUMBALL_TIMEOUT_SECONDS`

Env loading:
- Use `--env-file .env` for explicit loading.
- Without `--env-file`, script auto-tries `./.env` then `<skill-root>/.env`.

## Output Contract

Always return:
- `Freshness`: retrieval time and target object
- `Key deltas`: metric-level differences vs prior expectation
- `Impact`: why the delta matters for decision-making
- `Next step`: monitor, replace creator, or continue

## Failure Handling

- If platform identifiers are missing, request minimal required ID.
- If realtime endpoint returns no data, retry once and report fallback.
- If user asks for historical trend, hand off to monitoring skill.

## References

- `references/api-index.md`
- `references/request-response.md`
- `references/operations.json`
