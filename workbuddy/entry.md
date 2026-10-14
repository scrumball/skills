---
name: scrumball-influencer-marketing
description: "Get started with Scrumball, the influencer marketing platform (网红营销平台): finding creators / 网红 / 达人 / KOL, outreach (建联), creator emails (回信) and team usage (统计). Use only when the user wants Scrumball or influencer marketing help and no Scrumball tools are available yet; once the Scrumball connector is connected, its own skills take over. 例如「怎么用 Scrumball 找网红」。"
---

<!-- WorkBuddy 技能市场上架的入口 skill：负责被用户发现，并引导安装 Scrumball 连接器。
     不写工具用法（那在连接器自带的 skill 里），名字也与连接器里的 4 个 skill 不重名，两边同时安装不冲突。 -->

# Scrumball influencer marketing

Scrumball is an influencer marketing platform. With the Scrumball connector, you can help the user:

- find creators on YouTube, Instagram and TikTok by niche, country, follower range and language, compare them, save them to collections and, with the user's OK, unlock contact emails;
- follow outreach campaigns: which creators replied, who quoted a price, which emails need a reply today, how a campaign is performing;
- review usage for each team member or the whole company: rankings, trends, spending and remaining credits.

## What to do

1. **If Scrumball tools are already available** (for example `search_creators`, `get_quota_status` or `outreach_*` tools): this skill has nothing more to add. Follow the skills that came with the Scrumball connector (`scrumball-creators`, `scrumball-outreach`, `scrumball-stats`) and answer the user's request.
2. **If no Scrumball tools are available**: tell the user that Scrumball works through its connector, then ask them to open WorkBuddy's connector marketplace (连接器市场), search for **Scrumball**, install it and connect it. A browser page opens; they sign in with their Scrumball account. No API key is needed.
3. Before they sign in, tell them two things:
   - the sign-in page lists permissions as checkboxes; **"Spend your unlock credits to reveal creator emails / 代你消耗解锁额度获取网红邮箱"** lets the AI spend paid, non-refundable credits, and they can untick it;
   - tool calls use Scrumball call credits; each tool's description states its cost.
4. After they connect, continue with their original request.

Do not make up creator data, campaign results or statistics before the connector is connected. If the user has no Scrumball account, they can sign up on the Scrumball website.
