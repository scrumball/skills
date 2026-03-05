# scrumball-skills

Scrumball influencer skills with self-contained execution scripts per skill.

## Prerequisites

- Python 3.9+
- Network access to `SCRUMBALL_BASE_URL`
- A valid `SCRUMBALL_API_KEY`

## Install

Install from registry/repo using your installer, for example:

```bash
npx skills add scrumball/skills
```

You can install one skill or all skills.

## Quick Start (Local)

```bash
cp .env.example .env
# edit .env with your real base URL and API key

python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env list
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env call --operation ping
```

## Environment Variables

Required:
- `SCRUMBALL_BASE_URL`
- `SCRUMBALL_API_KEY`

Optional:
- `SCRUMBALL_AUTH_PREFIX`
- `SCRUMBALL_TIMEOUT_SECONDS`

Example values are in `.env.example`.

## Security

- Never commit real credentials to this repository.
- Keep secrets in local `.env` only, and rotate keys immediately if exposed.
- The repository should only contain placeholder values (for example in `.env.example`).

## Skill Call Examples

Run from repository root with `--env-file .env`:

```bash
# 1) Lead discovery
python3 skills/influencer-lead-discovery/scripts/execute_operation.py --env-file .env call --operation search_tiktok_user --body '{"query":"nike","page":1,"page_size":10}'

# 2) Audience fit scoring
python3 skills/influencer-audience-fit-scoring/scripts/execute_operation.py --env-file .env call --operation audience_tiktok_interest --query '{"unique_id":"nike"}'

# 3) Realtime enrichment
python3 skills/influencer-realtime-enrichment/scripts/execute_operation.py --env-file .env call --operation tiktok_realtime_user_info --query '{"unique_id":"nike"}'

# 4) Campaign monitoring
python3 skills/influencer-campaign-monitoring/scripts/execute_operation.py --env-file .env call --operation list_monitor_tasks

# 5) Commerce intel
python3 skills/influencer-commerce-intel/scripts/execute_operation.py --env-file .env call --operation tiktok_user_shop_sale --query '{"unique_id":"nike"}'
```

## Troubleshooting

- `SCRUMBALL_BASE_URL is required`: set `SCRUMBALL_BASE_URL` in `.env`.
- `SCRUMBALL_API_KEY is required`: set `SCRUMBALL_API_KEY` in `.env`.
- `Missing required ...`: check required query/body fields for that operation.
- Network/DNS errors: verify gateway reachability and local network.

## Skill Folders

- `skills/influencer-lead-discovery`
- `skills/influencer-audience-fit-scoring`
- `skills/influencer-realtime-enrichment`
- `skills/influencer-campaign-monitoring`
- `skills/influencer-commerce-intel`

Each skill is self-contained and includes:
- `SKILL.md`
- `agents/openai.yaml`
- `references/` (api index, request/response hints, operations)
- `scripts/execute_operation.py`

## License

MIT. See `LICENSE`.
