# Scrumball Skills

[English](README.md)

让 AI 助手使用 **Scrumball 网红营销平台**：找网红、跟进建联任务、处理与网红的往来邮件、查看使用统计。

在浏览器里用 Scrumball 账号登录授权即可，不需要 API Key。

## 安装

**任何支持 Agent Skills 的 AI 助手**（Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot 等）：

```bash
npx skills add scrumball/skills
```

装好后直接对 AI 说「连接 Scrumball」，或者直接问「今天有哪些网红回信需要我处理？」。`scrumball-connect` 会帮你把 Scrumball 接入当前助手，并打开登录授权页面。

**Claude Code 插件**（Skill 和连接一步装好）：

```
/plugin marketplace add scrumball/skills
/plugin install scrumball@scrumball
```

**Claude.ai / Claude Desktop**：先上传本仓库的 Skill，再对 Claude 说「连接 Scrumball」，它会给出要在「Customize → Connectors」里添加的地址。

## 包含的 Skill

| Skill | 用途 |
|---|---|
| `scrumball-connect` | 接入 Scrumball、登录授权、授权问题排查 |
| `scrumball-creators` | 找网红、评估网红、存入收藏夹、解锁联系邮箱 |
| `scrumball-outreach` | 建联任务、建联数据看板、消息工单（与网红的往来邮件） |
| `scrumball-stats` | 按成员或全公司的使用统计、排行、趋势、消费与剩余额度 |

## 可以这样问

- 「今天有哪些回信要我处理？超时没回的排前面。」
- 「『夏季上新』这个任务里，哪些网红报了价？」
- 「最近 30 天建联效果怎么样？」
- 「哪些会话超过一周没动静了？」
- 「我还剩多少解锁额度？」

AI 只读取你的数据；发邮件、建任务等操作仍在 Scrumball 网页完成，AI 会给出对应页面的链接。

## 使用前须知

- 需要 Scrumball 账号（公司主账号或子账号）。AI 能看到的数据跟随登录账号：主账号看全公司，子账号看自己的。使用统计需要会员有效。
- AI 每调用一次工具都会消耗 Scrumball 调用额度（搜索比查询消耗多）。解锁网红邮箱会消耗解锁额度，AI 一定会先征得你的同意。
- 授权页上由你勾选允许 AI 做什么：网红搜索与收藏、消耗解锁额度、查看团队使用与消费、查看建联任务与往来邮件。不想让 AI 花解锁额度，就取消勾选那一项。随时可以重新授权调整。

## License

MIT
