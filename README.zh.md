# Scrumball Skills

[English](README.md)

让 AI 助手使用 **Scrumball 网红营销平台**：找网红、跟进建联任务、梳理与网红的往来邮件、查看使用统计。

在浏览器里用 Scrumball 账号登录授权即可，不需要 API Key。

## 使用前须知

- 需要 Scrumball 账号（公司主账号或子账号）。AI 能看到的数据跟随登录账号：主账号看全公司，子账号看自己的。使用统计需要会员有效；成员列表和排行需要主账号。
- AI 每调用一次工具都会消耗 Scrumball 调用额度：搜索 3 个，查看一个网红或一个会话 1 个，几分钟内重复同样的搜索不扣额度。
- 解锁网红邮箱会消耗解锁额度，扣了不退。装好 Skill 后，AI 会先告诉你要用多少额度，等你同意再解锁。
- 授权页上由你勾选允许 AI 做什么。想自己决定解锁，就取消勾选 **「代你消耗解锁额度获取网红邮箱」**。之后想改，重新登录授权即可；如果没生效，对 AI 说「修复 Scrumball 连接」。

## 安装

### Claude Code

两种方式二选一，不要同时装。

**插件（推荐）**：Skill 和 Scrumball 连接一起装好。

```
/plugin marketplace add scrumball/skills
/plugin install scrumball@scrumball
```

重启 Claude Code 后输入 `/mcp`，选择显示为 `plugin:scrumball:scrumball` 的服务，点 **Authenticate**，浏览器会打开登录页面。

**只装 Skill**：按下一节操作。

### Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot 等支持 Agent Skills 的 AI 助手

需要 Node.js 18 或更高版本。

```bash
npx skills add scrumball/skills -g
```

`-g` 表示装到当前用户下，在任何目录打开 AI 都能用。如果询问装到哪些助手，选你在用的即可。

装好后直接问 AI 和 Scrumball 有关的问题，例如「今天有哪些网红回信需要我处理？」。第一次使用时，`scrumball-connect` 会征求你的同意，把 Scrumball 接入当前助手，并告诉你怎么登录。Claude Code 里：重启 Claude Code，输入 `/mcp`，选择 `scrumball`，点 **Authenticate**。

### Claude.ai 与 Claude Desktop

1. **添加连接器**：**Customize → Connectors → + Add → Add custom connector**，名称填 `Scrumball`，地址填 `https://api.scrumball.ai/mcp/server`，然后点 **Connect** 登录。Team / Enterprise 套餐由 Owner 在 **Organization settings → Connectors** 添加，成员各自点 **Connect**。
2. **上传 Skill（推荐）**：Skill 会引导 AI 正确使用，包括解锁邮箱前的额度确认。
   1. 在 **Settings → Capabilities** 打开 **Code execution and file creation**。
   2. 下载本仓库（**Code → Download ZIP**）并解压。
   3. 在 `skills` 文件夹里，把四个文件夹分别单独压缩（Mac：右键 → 压缩；Windows：右键 → 发送到 → 压缩(zipped)文件夹）。每个 zip 里要包含文件夹本身，例如 `scrumball-creators/SKILL.md`。
   4. 逐个在 **Customize → Skills → + → Create skill → Upload a skill** 上传。

### 确认装好了

问一句「我还剩多少解锁额度？」，AI 能答出你的数字，就说明已经连上。

## 更新

| 安装方式 | 更新方式 |
|---|---|
| Claude Code 插件 | 在终端运行 `claude plugin marketplace update scrumball` 和 `claude plugin update scrumball@scrumball`，然后重启 Claude Code |
| `npx skills add` | `npx skills update` |
| Claude.ai 上传 | 重新上传新的 zip |

## 包含的 Skill

| Skill | 用途 |
|---|---|
| `scrumball-connect` | 接入 Scrumball、登录授权、授权问题排查 |
| `scrumball-creators` | 找网红、评估网红、存入收藏夹、解锁联系邮箱 |
| `scrumball-outreach` | 建联任务、建联数据看板、消息工单（与网红的往来邮件） |
| `scrumball-stats` | 按成员或全公司的使用统计、排行、趋势、消费与剩余额度 |

## 可以这样问

- 「帮我在 TikTok 上找 20 个美国美妆博主，粉丝 5 万到 50 万。」
- 「今天有哪些回信要我处理？超时没回的排前面。」
- 「『夏季上新』这个任务里，哪些网红报了价？」
- 「最近 30 天建联效果怎么样？」
- 「我还剩多少解锁额度？」

AI 可以搜索网红、存入收藏夹，经你同意后解锁邮箱。建联和统计只读：发邮件、建任务、改任务在 Scrumball 网页完成，AI 会给出对应页面的链接。

## License

MIT
