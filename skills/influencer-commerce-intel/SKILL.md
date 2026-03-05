---
name: influencer-commerce-intel
description: Commerce-focused intelligence for creator-led selling, especially TikTok Shop. Use when users ask to assess creator monetization performance, analyze goods/live/video-ad selling signals, inspect product detail, or compare commerce potential across creators.
---

# Influencer Commerce Intel

Analyze creator commerce performance and monetization potential.

## Quick Start

1. Confirm commerce objective (GMV growth, product seeding, ad ROI).
2. Collect creator identifier (`unique_id`) and optional product/video filters.
3. Pull sale/goods/live/ad signals from commerce endpoints.
4. Return actionable commerce recommendation.

## Workflow

1. Build commerce snapshot:
- Sale overview
- Goods list
- Live list
- Video ad list

2. Deep dive when needed:
- Fetch realtime product detail for top candidates.
- Identify winning categories and content formats.

3. Evaluate monetization potential:
- Judge consistency, conversion signals, and catalog quality.
- Provide partner recommendation and test plan.

## Tooling

Execution commands:
- List operations: `python3 scripts/execute_operation.py --env-file .env list`
- Sale snapshot: `python3 scripts/execute_operation.py --env-file .env call --operation tiktok_user_shop_sale --query '{"unique_id":"nike"}'`
- Goods list: `python3 scripts/execute_operation.py --env-file .env call --operation tiktok_user_shop_goods_list --query '{"unique_id":"nike","page":1,"page_size":20}'`


Required environment variables:
- `SCRUMBALL_BASE_URL`: API gateway base URL
- `SCRUMBALL_API_KEY`: unified API key
- Optional: `SCRUMBALL_AUTH_PREFIX`, `SCRUMBALL_TIMEOUT_SECONDS`

Env loading:
- Use `--env-file .env` for explicit loading.
- Without `--env-file`, script auto-tries `./.env` then `<skill-root>/.env`.

## Output Contract

Always return:
- `Commerce summary`: top performance signals
- `Opportunity`: product/category/content opportunity
- `Risk`: instability, low signal confidence, or limited sample
- `Next step`: pilot recommendation and expected KPI

## Failure Handling

- If commerce identifiers are incomplete, ask for `unique_id` first.
- If one commerce dimension is missing, continue with available dimensions and mark confidence.
- If user asks for broad discovery, hand off to lead-discovery skill.

## References

- `references/api-index.md`
- `references/request-response.md`
- `references/operations.json`
