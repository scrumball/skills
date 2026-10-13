# Scrumball Skills

[中文](README.zh.md)

Skills that let AI agents work with **Scrumball**, the influencer marketing platform: find creators, follow outreach campaigns, triage the creator inbox and review usage statistics.

You sign in with your Scrumball account in the browser. No API key.

## Before you start

- A Scrumball account: the company main account or a member account. The agent sees what that account sees: the main account sees the whole company, a member account sees its own data. Usage statistics need an active membership; the member list and rankings need the main account.
- Every tool call the agent makes uses Scrumball call credits: a search uses 3, viewing a creator or a conversation uses 1, and repeating the same search within a few minutes is free.
- Unlocking a creator's email uses an unlock credit and cannot be refunded. With the skills installed, the agent tells you how many credits it will use and waits for your OK.
- On the sign-in page you choose what the agent may do. To keep unlocking to yourself, untick **"Spend your unlock credits to reveal creator emails"**. To change your choice later, sign in again; if the change does not show, ask the agent to "fix my Scrumball connection".

## Install

### Claude Code

Pick one of the two ways, not both.

**Plugin (recommended):** installs the skills and the Scrumball connection together.

```
/plugin marketplace add scrumball/skills
/plugin install scrumball@scrumball
```

Restart Claude Code, type `/mcp`, choose the server listed as `plugin:scrumball:scrumball` and select **Authenticate**. A browser page opens for you to sign in.

**Skills only:** follow the next section.

### Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and other agents that support Agent Skills

Requires Node.js 18 or later.

```bash
npx skills add scrumball/skills -g
```

`-g` installs for your user account, so the skills work in every folder. If asked which agents to install to, pick the ones you use.

Then ask your agent anything about Scrumball, for example *"what creator emails need my reply today?"*. The first time, the `scrumball-connect` skill offers to add the Scrumball server to your agent and tells you how to sign in. In Claude Code: restart Claude Code, type `/mcp`, choose `scrumball` and select **Authenticate**.

### Claude.ai and Claude Desktop

1. **Add the connector:** **Customize → Connectors → + Add → Add custom connector**, name it `Scrumball`, enter `https://api.scrumball.ai/mcp/server`, then click **Connect** and sign in. On Team and Enterprise plans an Owner adds it under **Organization settings → Connectors**, and each member clicks **Connect**.
2. **Upload the skills (recommended):** they guide the agent, including the credit check before unlocking emails.
   1. Turn on **Settings → Capabilities → Code execution and file creation**.
   2. Download this repository (**Code → Download ZIP**) and unzip it.
   3. In the `skills` folder, compress each of the four folders on its own (Mac: right-click → Compress; Windows: right-click → Send to → Compressed (zipped) folder). Each zip must contain the folder, for example `scrumball-creators/SKILL.md`.
   4. Upload each zip under **Customize → Skills → + → Create skill → Upload a skill**.

### Check that it works

Ask *"How many unlock credits do I have left?"*. If the agent answers with your numbers, you are connected.

## Update

| Installed with | Update with |
|---|---|
| Claude Code plugin | run `claude plugin marketplace update scrumball` and `claude plugin update scrumball@scrumball` in a terminal, then restart Claude Code |
| `npx skills add` | `npx skills update` |
| Claude.ai upload | upload the new zips |

## Skills

| Skill | Use it for |
|---|---|
| `scrumball-connect` | Connecting your agent to Scrumball, signing in, fixing sign-in problems |
| `scrumball-creators` | Finding and evaluating creators, saving them to collections, unlocking contact emails |
| `scrumball-outreach` | Outreach tasks, the outreach dashboard and the inbox of email threads with creators |
| `scrumball-stats` | Usage statistics per member or company-wide, rankings, trends, spending and remaining credits |

## What you can ask

- "Find 20 US beauty creators on TikTok with 50k to 500k followers."
- "What needs my reply today? Overdue ones first."
- "Which creators in the *Summer Launch* campaign quoted a price?"
- "How did my outreach do in the last 30 days?"
- "How many unlock credits do I have left?"

The agent can search creators, save them to collections and, with your OK, unlock emails. Outreach and statistics are read-only: sending emails and creating or editing campaigns happen on the Scrumball website, and the agent gives you the link.

## License

MIT
