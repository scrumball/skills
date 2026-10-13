---
name: scrumball-connect
description: "Connect Scrumball, the influencer marketing platform (网红营销平台), to this AI client through MCP with a browser sign-in — no API key. Use when the user wants Scrumball data or actions (creators / 网红 / 达人 / KOL, outreach / 建联, inbox / 回信, statistics / 统计, credits / 额度) but no Scrumball tools are available yet, or a Scrumball tool fails with 401 / unauthorized / insufficient_scope, or an expected Scrumball capability is missing. 例如「连接 Scrumball」「Scrumball 授权失效了」「怎么在 AI 里用 Scrumball」。"
compatibility: Connects the Scrumball remote MCP server; other scrumball-* skills depend on it.
---

# Connect Scrumball

Scrumball exposes its data as a remote MCP server. Connecting is one configuration step plus a browser sign-in; the user never handles a token or API key.

## 1. Check whether it is already connected

Scrumball is connected if the tool list contains any tool from these families, whatever the server is called in this client:

- `search_creators`, `get_creator`, `get_quota_status`
- `employee_activity_overview`, `wallet_consumption`
- `outreach_inbox_summary` and other `outreach_*` tools

If some families are present but the one the user needs is missing, go to section 4 (missing capability).

If no Scrumball tools are present, check the client's MCP server list before adding anything (Claude Code: `claude mcp list`; Codex: `codex mcp list`; Gemini CLI: `gemini mcp list`; Cursor / VS Code: the MCP settings). A server named like `scrumball…`, or one whose URL ends in `/mcp/server`, that shows "needs authentication", "failed" or "disconnected" means it is added but not signed in: go to section 3.

Never add a second Scrumball server when one is already configured.

## 2. Add the server

Server URL (Streamable HTTP, OAuth sign-in):

```
https://api.scrumball.ai/mcp/server
```

If the environment variable `SCRUMBALL_MCP_URL` is set (check with `echo $SCRUMBALL_MCP_URL`; on Windows `echo %SCRUMBALL_MCP_URL%`), use its value instead of the URL above and tell the user which address you are using. Otherwise use the URL above.

Use the server name `scrumball`. Ask the user before changing their configuration, then do it for the client you are running in:

| Client | How to add |
|---|---|
| Claude Code | `claude mcp add -s user --transport http scrumball <URL>` |
| Codex CLI | `codex mcp add scrumball --url <URL>` |
| Gemini CLI | `gemini mcp add -s user --transport http scrumball <URL>` |
| Cursor | add to `~/.cursor/mcp.json`: `{"mcpServers": {"scrumball": {"url": "<URL>"}}}` |
| VS Code (Copilot) | add to the user `mcp.json`: `{"servers": {"scrumball": {"type": "http", "url": "<URL>"}}}` |
| Claude.ai / Claude Desktop | the user adds it: Customize → Connectors → + Add → Add custom connector, pasting the URL above (Team / Enterprise: an Owner adds it under Organization settings → Connectors, then each member clicks Connect). Give the user the URL. |
| Other clients | add a remote MCP server (HTTP / Streamable HTTP) with the URL above |

## 3. Sign in

New servers usually load only after the client restarts or reconnects. Then the user opens the sign-in page:

| Client | How to open the sign-in page |
|---|---|
| Claude Code | the user types `/mcp`, picks `scrumball` (listed as `plugin:scrumball:scrumball` when installed as a plugin), chooses Authenticate (restart Claude Code first if the server was just added) |
| Codex CLI | run `codex mcp login scrumball` |
| Gemini CLI | the user types `/mcp auth scrumball` |
| Cursor / VS Code | the login / Start button next to `scrumball` in the MCP settings |
| Claude.ai / Desktop | the Connect button on the connector |

You cannot run slash commands or click buttons for the user; tell them exactly what to type or click.

On the sign-in page the user logs in with their Scrumball account (the same one as on the website; company main accounts and member accounts both work) and approves access. The page lists the permissions as checkboxes; the user can untick any optional one:

| Permission on the page (English / 中文) | Lets the AI |
|---|---|
| View your account info / 读取你的账号基本信息 | read the account email, company and membership |
| Use creator search and collections / 使用网红搜索与收藏功能 | search creators, view profiles and posts, manage collections |
| Spend your unlock credits to reveal creator emails / 代你消耗解锁额度获取网红邮箱 | unlock creator emails — **spends paid credits, non-refundable** |
| View per-member usage and spending / 查看团队成员的使用与消费明细 | see each team member's activity, spending and ranking |
| View outreach campaigns and email threads / 查看建联任务与往来邮件 | read outreach tasks, the dashboard and email threads with creators |

Point out the credit-spending permission before the user approves; untick it to keep the AI from spending unlock credits. Only approved permissions are usable — tools for the others do not appear. After approval the tools appear; some clients need one more reconnect.

## 4. Troubleshooting

| Symptom | What to do |
|---|---|
| Scrumball tools cannot be found at all (找不到工具), although the server was added | The client has not loaded it or the user has not signed in yet: restart / reconnect the client, then sign in (section 3). If the server is not in the client's MCP list, add it (section 2). |
| 401 / unauthorized / token expired | Sign in again (section 3). |
| 403 `insufficient_scope`, or a capability is missing from the tool list | That permission was unticked at sign-in, or the capability was released after the last sign-in. Sign in again and keep it ticked; if it is still missing, remove the `scrumball` server and add it again (section 2). |
| `invalid_scope` on the sign-in page | Remove the `scrumball` server and add it again. |
| `access_denied` on the sign-in page | The account cannot authorize; use the company main account or a member account of the company. |
| Tools look outdated after a Scrumball update | The client cached the tool list; reconnect the server. |
| Membership error on statistics tools | Usage statistics need an active membership; renew on the Scrumball website. |
| A tool is "main account only" | The member list and rankings need the company main account; sign in with it. |
| Rate limit / daily limit reached | Wait and retry later; `get_quota_status` shows the remaining call credits. |
| First call fails with "connection reset" | Retry once; if it keeps failing, reconnect the server. |

## After connecting

Continue with the user's original request. Related skills: `scrumball-creators` (find and evaluate creators, collections, unlock emails), `scrumball-outreach` (outreach tasks, dashboard, inbox), `scrumball-stats` (usage statistics, spending, credits).
