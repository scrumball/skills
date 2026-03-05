---
name: influencer-lead-discovery
description: Cross-platform influencer discovery and shortlist building. Use when users ask to find creators by keyword/niche/region/engagement, search creator or content candidates, expand similar creators, inspect creator profiles and content history, or produce outreach-ready lead lists.
---

# Influencer Lead Discovery

Build decision-ready creator shortlists across TikTok, Instagram, and YouTube.

## Quick Start

1. Confirm target platform, market, and campaign goal.
2. Open `references/api-index.md` to select discovery and profile endpoints.
3. Open `references/request-response.md` if request fields are unclear.
4. Run calls via `scripts/execute_operation.py`.
5. Return ranked candidates with reasons and next action.

## Workflow

1. Define search intent:
- Brand/category keywords
- Geography/language
- Creator scale and engagement threshold

2. Run discovery first:
- Use `search_*` operations to produce candidate pools.
- Use pagination (`page`, `page_size`) for complete coverage.

3. Enrich shortlisted creators:
- Pull creator profile, content history, brand collab, hashtag engagement.
- Expand nearby options with `*_user_similar`.

4. Score and rank:
- Rank by relevance, consistency, and partnership potential.
- Keep ranking logic explicit in output.

## Tooling

Execution commands:
- List operations: `python3 scripts/execute_operation.py --env-file .env list`
- Filter by tag: `python3 scripts/execute_operation.py --env-file .env list --tag search`
- Example search: `python3 scripts/execute_operation.py --env-file .env call --operation search_tiktok_user --body '{"query":"nike","page":1,"page_size":10}'`
- Example enrich: `python3 scripts/execute_operation.py --env-file .env call --operation tiktok_db_user_info --query '{"unique_id":"nike"}'`


Required environment variables:
- `SCRUMBALL_BASE_URL`: API gateway base URL
- `SCRUMBALL_API_KEY`: unified API key
- Optional: `SCRUMBALL_AUTH_PREFIX`, `SCRUMBALL_TIMEOUT_SECONDS`

Env loading:
- Use `--env-file .env` for explicit loading.
- Without `--env-file`, script auto-tries `./.env` then `<skill-root>/.env`.

## Output Contract

Always return:
- `Top candidates`: ordered list with platform + identifier
- `Why selected`: 2-3 evidence points per candidate
- `Risks`: data gaps or quality caveats
- `Next step`: outreach/testing recommendation

## Failure Handling

- If required IDs are missing, ask only for minimal fields.
- If no results, relax one filter at a time and report what changed.
- If API fails, include failed operationId and retry suggestion.

## References

- `references/api-index.md`: endpoint inventory for this skill
- `references/request-response.md`: required params and body hints
- `references/operations.json`: operation metadata used by the script
