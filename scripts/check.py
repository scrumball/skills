#!/usr/bin/env python3
"""发布前检查：skill 格式、MCP 地址只有一个来源、不出现旧品牌名与内部地址、引用的 tool 名真实存在。

用法：python3 scripts/check.py    （任一项不通过退出码 1）
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []

# 1. MCP 地址：以 .mcp.json 为准，connect skill 必须与之一致，其它文件不得再写地址（换域名只改这两处）
url = json.loads((ROOT / '.mcp.json').read_text())['mcpServers']['scrumball']['url']
connect = (ROOT / 'skills/scrumball-connect/SKILL.md').read_text()
if url not in connect:
    errors.append(f'scrumball-connect 里的地址与 .mcp.json 不一致：{url}')
text_files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.suffix in ('.md', '.json', '.yaml', '.yml', '.txt')]
for p in text_files:
    rel = p.relative_to(ROOT).as_posix()
    s = p.read_text(errors='ignore')
    if rel not in ('.mcp.json', 'skills/scrumball-connect/SKILL.md'):
        for m in re.findall(r'https?://api\.[a-z0-9.-]+/mcp/server', s):
            errors.append(f'{rel}: MCP 地址只能写在 .mcp.json 与 scrumball-connect，发现 {m}')
    # 旧品牌名 / 旧域名与内部测试环境不得对外出现（2026-10 已换到 api.scrumball.ai）
    if re.search(r'kol\s*masters', s, re.I):
        errors.append(f'{rel}: 出现旧品牌名或旧域名 KOL Masters')
    if re.search(r'coredesk|kolpalybook', s, re.I):
        errors.append(f'{rel}: 出现内部测试环境地址')

# 2. skill 格式：frontmatter 有 name/description，name 与目录名一致，description 不超长
tools = {l.strip() for l in (ROOT / 'scripts/tools.txt').read_text().splitlines() if l.strip() and not l.startswith('#')}
# 形似 tool 名但其实是参数取值的标识（团队统计的 metric 取值）
NON_TOOLS = {'wallet_spend'}
tool_pat = re.compile(r'`((?:outreach|search|get|list|unlock|create|add|remove|check|employee|module|wallet|activity)_[a-z_]+)`')
for skill in sorted((ROOT / 'skills').glob('*/SKILL.md')):
    s = skill.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
    name = skill.parent.name
    if not m:
        errors.append(f'{name}: 缺少 frontmatter'); continue
    fm = dict(re.findall(r'^(\w+):\s*(.+)$', m.group(1), re.M))
    # 未加引号的值里出现「冒号+空格」是非法 YAML，安装器会静默跳过这个 skill
    for k, v in fm.items():
        if not v.startswith(('"', "'")) and ': ' in v:
            errors.append(f'{name}: frontmatter {k} 含「: 」但未加引号，YAML 解析会失败')
    fm = {k: v.strip('"').strip("'") for k, v in fm.items()}
    if fm.get('name') != name:
        errors.append(f'{name}: frontmatter name={fm.get("name")} 与目录名不一致')
    if not fm.get('description') or len(fm['description']) > 1024:
        errors.append(f'{name}: description 缺失或超过 1024 字符')
    # 3. 引用的 tool 名必须存在（防止服务端改名后 skill 指向不存在的工具）
    for t in sorted(set(tool_pat.findall(s))):
        # 以 _url / _id / _ids 结尾的是返回字段或参数名（如 create_task_url），不是 tool
        if re.search(r'_(url|id|ids)$', t) or t in NON_TOOLS:
            continue
        if t not in tools:
            errors.append(f'{name}: 引用了不存在的 tool `{t}`')

if errors:
    print('\n'.join('FAIL ' + e for e in errors)); sys.exit(1)
print(f'OK：{len(list((ROOT / "skills").glob("*/SKILL.md")))} 个 skill 通过检查，MCP 地址 {url}')
