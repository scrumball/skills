---
name: scrumball-stats
description: "Usage statistics, spending and credits on Scrumball, the influencer marketing platform (网红营销平台) — email unlocks, saved creators, outreach tasks, emails sent and replied, per member or for the whole company; rankings, trends over days / weeks / months, wallet spending and remaining credits. Use for \"how much did we do this week\", \"who sent the most outreach emails\", \"how much did we spend this month\", \"how many credits are left\", \"write a weekly report\". 例如「这周数据怎么样」「谁发的建联邮件最多」「这个月花了多少钱」「还剩多少额度」「帮我写个周报」。"
compatibility: Requires the Scrumball MCP server (see scrumball-connect).
---

# Scrumball Stats

Requires the Scrumball tools (`employee_activity_overview`, `wallet_consumption`, …). If they are missing, follow the `scrumball-connect` skill first.

## Whose data you see

Data follows the account the user signed in with:

- **Company main account**: the whole company, every member separately or combined. `list_employees` and `employee_ranking` work only here.
- **Member account**: that member's own data.

Statistics tools also need an active Scrumball membership. If a tool says the account or membership does not allow it, explain that plainly instead of retrying.

## Periods

Most tools default to the last 30 days. `employee_ranking` and `activity_trend` require `date_range` — pass the last 30 days when the user gave no period. Turn "this week", "September", "last month" into exact dates and always say which dates you used.

## Scenarios

### "How much did we do this week / this month?"

1. `employee_activity_overview` (no `operator_id` = everyone visible to this account).
2. `module_usage_stats` with `group_by=operator` for the per-member breakdown (main account).
3. Present a table, then two or three observations, for example who carried most of the outreach or who unlocked emails but sent nothing. A reply ratio here is `email_reply / email_send`, counted in emails; it is not the outreach dashboard's `reply_rate`, which counts people. Name it accordingly.

### "Who did the most / least?"

`employee_ranking` with the metric that matches the question (`email_send` for outreach effort, `email_reply` for replies received, `wallet_spend` for spending) and a `date_range`.

For "least active", call `list_employees` without `active_since` and look at the last active date and the 30-day action count; members with no recent activity show no last active date.

### "Is it going up or down?"

`activity_trend` with a metric, `granularity` (day / week / month) and a `date_range` (up to 92 days by day; use month for calendar-month comparisons). Add `operator_id` for one member. Describe the direction and any sharp change, with dates.

### "How much did we spend?"

`wallet_consumption` with `group_by` total, operator or day. Report the amount exactly as returned, without adding a currency symbol, and the period; spending includes amounts frozen for pending orders.

### "How many credits are left?"

`get_quota_status`. Report separately: call credits (used by every AI tool call, reset each cycle, with a daily cap) and email unlock credits (membership allowance plus top-ups, non-refundable once spent), and the membership state. Top-ups happen on the Scrumball website.

### Weekly report

1. The "how much did we do" scenario for the last 7 days and the 7 days before.
2. Outreach results from the `scrumball-outreach` skill: `outreach_dashboard_overview` for the funnel, `outreach_inbox_summary` with `group_by=operator` for unanswered replies per member.
3. Write: headline numbers with week-over-week change, standout contributors, where help is needed (unanswered replies piling up, activity dropping), spending, credits left.

## Ground rules

- These numbers describe individual people's work. State them factually; do not judge anyone. Give the numbers and let the user draw conclusions.
- Different metrics come from different sources; do not add them together.
- Read-only: managing members and buying credits happen on the Scrumball website.
