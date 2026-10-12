# Scrumball Skills

[中文](README.zh.md)

Skills that let AI agents work with **Scrumball**, the influencer marketing platform: find creators, follow outreach campaigns, triage the creator inbox and review usage statistics.

Sign in with your Scrumball account in the browser. No API key.

## Install

**Any agent that supports Agent Skills** (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot…):

```bash
npx skills add scrumball/skills
```

Then ask your agent something like *"connect Scrumball"* or just *"what creator emails need my reply today?"*. The `scrumball-connect` skill adds the Scrumball server to your agent and opens the sign-in page.

**Claude Code plugin** (skills and connection in one step):

```
/plugin marketplace add scrumball/skills
/plugin install scrumball@scrumball
```

**Claude.ai / Claude Desktop**: upload the skills from this repository, then ask Claude to *"connect Scrumball"*; it gives you the address to add under Customize → Connectors.

## Skills

| Skill | Use it for |
|---|---|
| `scrumball-connect` | Connecting your agent to Scrumball, signing in, fixing sign-in problems |
| `scrumball-creators` | Finding and evaluating creators, saving them to collections, unlocking contact emails |
| `scrumball-outreach` | Outreach tasks, the outreach dashboard and the inbox of email threads with creators |
| `scrumball-stats` | Usage statistics per member or company-wide, rankings, trends, spending and remaining credits |

## What you can ask

- "What needs my reply today? Overdue ones first."
- "Which creators in the *Summer Launch* campaign quoted a price?"
- "How did my outreach do in the last 30 days?"
- "Which conversations have gone quiet for more than a week?"
- "How many unlock credits do I have left?"

The agent reads your data; sending emails, creating campaigns and other changes stay on the Scrumball website, and the agent gives you the link.

## Before you start

- A Scrumball account (company main account or member account). What the agent can see follows that account: the main account sees the whole company, a member account sees its own data. Usage statistics need an active membership.
- Every tool call the agent makes uses your Scrumball call credits (a search uses more than a lookup). Unlocking a creator's email uses an unlock credit and is never done without asking you first.
- On the sign-in page you tick what the agent may do: creator search and collections, spending unlock credits, team usage and spending, outreach tasks and emails. Untick spending if you want to unlock emails yourself. You can sign in again any time to change it.

## License

MIT
