# Scrumball Skills

[中文](README.zh.md)

Skills that let AI agents work with **Scrumball**, the influencer marketing platform: find creators, follow outreach, triage the creator inbox, review usage statistics and performance, manage creator resources, and review promotion campaigns and approvals.

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
   3. In the `skills` folder, compress each folder on its own (Mac: right-click → Compress; Windows: right-click → Send to → Compressed (zipped) folder). Each zip must contain the folder, for example `scrumball-creators/SKILL.md`.
   4. Upload each zip under **Customize → Skills → + → Create skill → Upload a skill**.

### WorkBuddy, Trae, CodeBuddy and other agents

Each agent names this differently: WorkBuddy calls it a connector (连接器); Trae, CodeBuddy and others call it an MCP server. The steps are the same: add a remote server, then sign in to Scrumball in your browser.

**WorkBuddy:** search for **Scrumball** in the connector marketplace, install it and sign in when prompted. If it is not listed, add a custom connector with the settings below.

**Other agents:** add a remote server in the MCP or connector settings:

| Field | Value |
|---|---|
| Name | `Scrumball` |
| Type / transport | Streamable HTTP (sometimes shown as HTTP or Remote) |
| URL | `https://api.scrumball.ai/mcp/server` |
| Token, API key, headers | Leave empty |

After saving, the agent opens a sign-in page in your browser. Sign in with your Scrumball account and approve.

If the settings only accept a token or API key and no browser sign-in page opens, that agent does not support browser sign-in yet and cannot connect to Scrumball. Scrumball does not issue API keys.

If the agent supports Agent Skills, then run `npx skills add scrumball/skills -g` to install the skills. Scrumball works without them; with them the agent uses it more accurately.

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
| `scrumball-tracking` | Performance reports and post tracking, read-only |
| `scrumball-resources` | Finding and adding creator resources, updating tags, remarks, status and custom fields with permission |
| `scrumball-campaigns` | Promotion campaigns and creator collaborations, read-only in external clients |
| `scrumball-approvals` | Campaign approval applications and flows, read-only in external clients |

## What you can ask

- "Find 20 US beauty creators on TikTok with 50k to 500k followers."
- "What needs my reply today? Overdue ones first."
- "Which creators in the *Summer Launch* campaign quoted a price?"
- "How did my outreach do in the last 30 days?"
- "How many unlock credits do I have left?"

The agent can search creators, save them to collections and, with your OK, unlock emails. Resource records can be added or edited with `resource:write` permission. Outreach, statistics, tracking, promotion campaigns and approvals are read-only in external clients.

## License

MIT
