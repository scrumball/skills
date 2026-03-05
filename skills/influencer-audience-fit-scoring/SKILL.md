---
name: influencer-audience-fit-scoring
description: Audience-fit analysis for pre-campaign decision making. Use when users ask to evaluate creator audience quality or fit by geography/language/age/gender/interests/behavior/authenticity/rating-tier, compare creators on audience alignment, or justify creator selection with data-backed scoring.
---

# Influencer Audience Fit Scoring

Evaluate whether a creator's audience matches campaign targeting.

## Quick Start

1. Confirm campaign ICP (region, age, gender, interest, language).
2. Select platform and creator identifier (`unique_id`, `username`, `channel_id`).
3. Pull audience dimensions using operations in `references/api-index.md`.
4. Compute and explain fit score drivers.
5. Return recommendation: approve / test / reject.

## Workflow

1. Build target profile:

- Define must-have constraints (hard filters).
- Define preference signals (soft weights).

1. Pull audience dimensions:

- Geography, language, age, gender
- Interest and interaction behavior
- Follower authenticity and rating tier

1. Score consistently:

- Use transparent weighted scoring.
- Separate match score from data confidence.

1. Compare candidates:

- Normalize comparisons across same platform.
- Highlight strongest and weakest dimensions.

## Tooling

Execution commands:

- List operations: `python3 scripts/execute_operation.py --env-file .env list`
- Example dimension call: `python3 scripts/execute_operation.py --env-file .env call --operation audience_tiktok_interest --query '{"unique_id":"nike"}'`
- Example language call: `python3 scripts/execute_operation.py --env-file .env call --operation audience_youtube_language --query '{"channel_id":"UC_x5XG1OV2P6uZZ5FSM9Ttw"}'`


Required environment variables:
- `SCRUMBALL_BASE_URL`: API gateway base URL
- `SCRUMBALL_API_KEY`: unified API key
- Optional: `SCRUMBALL_AUTH_PREFIX`, `SCRUMBALL_TIMEOUT_SECONDS`

Env loading:
- Use `--env-file .env` for explicit loading.
- Without `--env-file`, script auto-tries `./.env` then `<skill-root>/.env`.


## Output Contract

Always return:

- `Fit score`: numeric score and confidence
- `Score breakdown`: geography/language/age/gender/interest/authenticity
- `Decision`: go / test / no-go
- `Action`: what to validate next

## Failure Handling

- If target profile is vague, ask for ICP before scoring.
- If one dimension is missing, continue scoring and lower confidence.
- If cross-platform comparison is requested, warn about comparability limits.

## References

- `references/api-index.md`
- `references/request-response.md`
- `references/operations.json`
