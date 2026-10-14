---
name: scrumball-connect
description: "Sign in to and troubleshoot the Scrumball connector (Scrumball 网红营销平台) in WorkBuddy. Use when Scrumball tools are missing, a Scrumball tool fails with 401 / unauthorized / insufficient_scope, or an expected Scrumball capability is missing. 例如「连接 Scrumball」「Scrumball 授权失效了」「Scrumball 工具找不到」。"
---

<!-- WorkBuddy 连接器包专用的 scrumball-connect：服务由连接器自带，这里只讲登录和排查，不教 AI 再添加服务。
     打包时替换 skills/scrumball-connect；故意不叫 SKILL.md，免得 npx skills add 把它当成第二个同名 skill。 -->

# Scrumball connector in WorkBuddy

In WorkBuddy, Scrumball is installed as a connector. The connector already contains the server configuration, so never add a Scrumball MCP server yourself and never ask the user for a token or API key. Signing in happens in the browser with the user's Scrumball account.

## 1. Check the tools

Scrumball is connected if the tool list contains any of: `search_creators`, `get_creator`, `get_quota_status`, `employee_activity_overview`, `wallet_consumption`, or `outreach_*` tools.

If none are present, the connector is not installed or not signed in: ask the user to open WorkBuddy's connector marketplace (连接器市场), search for **Scrumball**, install it if needed and connect it. A browser page opens for signing in.

If the user also added Scrumball by hand earlier as a custom MCP server, suggest removing that one so the tools are not listed twice.

## 2. Signing in

The user logs in with their Scrumball account (the same one as on the website; company main accounts and member accounts both work) and approves access. The page lists the permissions as checkboxes; the user can untick any optional one:

| Permission on the page (English / 中文) | Lets the AI |
|---|---|
| View your account info / 读取你的账号基本信息 | read the account email, company and membership |
| Use creator search and collections / 使用网红搜索与收藏功能 | search creators, view profiles and posts, manage collections |
| Spend your unlock credits to reveal creator emails / 代你消耗解锁额度获取网红邮箱 | unlock creator emails — **spends paid credits, non-refundable** |
| View per-member usage and spending / 查看团队成员的使用与消费明细 | see each team member's activity, spending and ranking |
| View outreach campaigns and email threads / 查看建联任务与往来邮件 | read outreach tasks, the dashboard and email threads with creators |

Point out the credit-spending permission before the user approves; untick it to keep the AI from spending unlock credits. Only approved permissions are usable — tools for the others do not appear.

You cannot click for the user; tell them exactly where to go.

## 3. Troubleshooting

| Symptom | What to do |
|---|---|
| No Scrumball tools at all | Install or connect the Scrumball connector (section 1). |
| 401 / unauthorized / sign-in expired | Reconnect / re-authorize the Scrumball connector and sign in again. |
| 403 `insufficient_scope`, or a capability is missing | That permission was unticked at sign-in, or the capability was released after the last sign-in. Reconnect / re-authorize the Scrumball connector and keep the permission ticked. If it is still missing, uninstall the Scrumball connector and install it again. |
| `invalid_scope` on the sign-in page | Uninstall the Scrumball connector and install it again. |
| `access_denied` on the sign-in page | The account cannot authorize; use the company main account or a member account of the company. |
| Tools look outdated after a Scrumball update | Reconnect the connector. |
| Membership error on statistics tools | Usage statistics need an active membership; renew on the Scrumball website. |
| A tool is "main account only" | The member list and rankings need the company main account; sign in with it. |
| Rate limit / daily limit reached | Wait and retry later; `get_quota_status` shows the remaining call credits. |

## After connecting

Continue with the user's original request. Related skills: `scrumball-creators` (find and evaluate creators, collections, unlock emails), `scrumball-outreach` (outreach tasks, dashboard, inbox), `scrumball-stats` (usage statistics, spending, credits).
