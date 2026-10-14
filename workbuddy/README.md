# WorkBuddy 上架包

这个目录生成 WorkBuddy 的两个上架包：连接器市场的连接器包和技能市场的入口 skill。用户安装不需要看这里。

## 生成

```bash
python3 scripts/check.py        # 需要本地 scripts/.deny-terms（不进 git）
python3 workbuddy/build.py      # 需要 workbuddy/icon.svg，或用 --icon 指定
```

产物在 `dist/workbuddy/`（不进 git）：

| 文件 | 提交到 |
|---|---|
| `scrumball-connector-<版本>.zip` | WorkBuddy 开放平台：连接器 |
| `scrumball-influencer-marketing-<版本>.zip` | WorkBuddy 开放平台：技能 |

## 文件

| 文件 | 作用 |
|---|---|
| `connector-meta.json` | 连接器名称、描述、示例；`version` 必须与 `package.json` 一致 |
| `mcp.json` | 连接器的 MCP 配置；地址必须与根目录 `.mcp.json` 一致 |
| `skills.json` | 打包时给每个 skill 补的 WorkBuddy 字段（中英文介绍、展示名、author） |
| `connect.md` | WorkBuddy 版 `scrumball-connect`，打包时替换 `skills/scrumball-connect` |
| `entry.md` | 技能市场入口 skill，只负责介绍和引导安装连接器 |
| `build.py` | 先跑 `scripts/check.py`，再从 `skills/` 生成两个 zip |

`connect.md` 和 `entry.md` 不能改名为 `SKILL.md`，否则 `npx skills add` 会把它们当成普通 skill 装给用户。

## 规则

- skill 正文只改 `skills/`，这里不放副本。
- 连接器先上架或与入口 skill 同时上架，入口 skill 不能先上。
- 入口 skill 不写工具用法，名字不能和 `skills/` 下的重名（`check.py` 会检查）。

## 首次上架前要核实的

在 WorkBuddy 4.24 或更高版本里，装一次本地打出来的连接器包，逐项确认：

- [ ] 完整走通一次：连接 → 浏览器登录授权 → 跳回 WorkBuddy → 调一次 `get_quota_status` 能返回数据。回调地址是 `workbuddy://workbuddy/mcp/connector%3Ascrumball/oauth/callback`；被拒时会回退到 `127.0.0.1`，两种都要通。
- [ ] 卸载后重装，会重新注册客户端：`connect.md` 里遇到 `invalid_scope` 的处理办法就是「卸载重装」，这一条成立它才有用。
- [ ] `connect.md`、`entry.md` 里写的「连接器市场」「重新连接 / 重新授权」，和客户端界面上的叫法一致。
- [ ] zip 根目录要不要多一层 `scrumball/` 文件夹：问开放平台或者上传试一次。
- [ ] `skills.json` 的 `author` 写入驻主体的名称；`category` 拿到官方的分类列表后再补。
