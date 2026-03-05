# scrumball-skills

Scrumball influencer skills with self-contained execution scripts per skill.

## Install

Install from registry/repo using your installer, for example:

```bash
npx skills add scrumball/skills
```

You can install one skill or all skills.

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

## Run a Single Installed Skill

Enter the installed skill folder and run:

```bash
python3 scripts/execute_operation.py --env-file .env list
python3 scripts/execute_operation.py --env-file .env call --operation <operationId> --query '{"key":"value"}'
python3 scripts/execute_operation.py --env-file .env call --operation <operationId> --body '{"key":"value"}'
```

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
