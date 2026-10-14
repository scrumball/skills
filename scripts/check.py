#!/usr/bin/env python3
"""发布前检查：skill 格式、MCP 地址只有一个来源、不出现本地禁用词、引用的 tool 名真实存在、WorkBuddy 包配置一致。

用法：python3 scripts/check.py                 （任一项不通过退出码 1）
      python3 scripts/check.py --scan-dir 目录  （只扫该目录下所有文件的禁用词，供 build.py 检查产物）
"""
import json, os, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []

# 1. MCP 地址：以 .mcp.json 为准；connect skill、两份 README（Claude.ai 用户要直接复制地址）、npm 迁移提示、
#    WorkBuddy 连接器的 mcp.json 必须与之一致，其它文件不得再写地址
url = json.loads((ROOT / '.mcp.json').read_text())['mcpServers']['scrumball']['url']
URL_FILES = ('.mcp.json', 'skills/scrumball-connect/SKILL.md', 'README.md', 'README.zh.md', 'bin/migrate.js', 'workbuddy/mcp.json')
for f in URL_FILES[1:]:
    body = (ROOT / f).read_text()
    if url not in body:
        errors.append(f'{f} 里的地址与 .mcp.json 不一致：{url}')
    for m in re.findall(r'https?://api\.[a-z0-9.-]+/mcp/server', body):
        if m != url:
            errors.append(f'{f}: 出现与 .mcp.json 不同的地址 {m}')
# 本地禁用词表：scripts/.deny-terms（已 gitignore，每行一个正则）+ 环境变量 SCRUMBALL_CHECK_DENY（逗号分隔）。
# 作用是防止旧品牌名、内部地址等再次进入公开仓库与上架包（历史提交里已有的不在此范围）；
# 词表不进仓库，免得检查脚本自己把这些词又公开一遍。没有词表直接失败，避免新机器上「检查全过」其实什么都没查。
DENY_FILE = ROOT / 'scripts/.deny-terms'
raw = [l.strip() for l in (DENY_FILE.read_text().splitlines() if DENY_FILE.exists() else [])]
raw += [t.strip() for t in os.environ.get('SCRUMBALL_CHECK_DENY', '').split(',')]
DENY = []
for t in raw:
    if not t or t.startswith('#'):
        continue
    try:
        DENY.append(re.compile(t, re.I))
    except re.error as e:
        errors.append(f'禁用词表里的正则写错了：{t}（{e}）')
if not DENY and not errors:
    errors.append('缺少本地禁用词表：创建 scripts/.deny-terms（每行一个正则）或设置 SCRUMBALL_CHECK_DENY')


def deny_hits(rel, s):
    return [f'{rel}: 出现本地禁用词表里的词（{pat.pattern}）' for pat in DENY if pat.search(s)]


# --scan-dir DIR：只对目录下所有文件做禁用词扫描（build.py 打包后扫产物，含 svg 图标里的元数据）
if len(sys.argv) == 3 and sys.argv[1] == '--scan-dir':
    d = pathlib.Path(sys.argv[2]).resolve()
    for p in sorted(d.rglob('*')):
        if p.is_file():
            errors += deny_hits(p.relative_to(d).as_posix(), p.read_bytes().decode('utf-8', 'ignore'))
    if errors:
        print('\n'.join('FAIL ' + e for e in errors)); sys.exit(1)
    print(f'OK：{d} 未发现禁用词'); sys.exit(0)

# 只扫会进仓库的文件（已跟踪 + 未跟踪但没被忽略的），本地虚拟环境、缓存、打包产物不扫
listed = subprocess.run(['git', 'ls-files', '-co', '--exclude-standard'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split('\n')
text_files = [ROOT / f for f in listed if f and (ROOT / f).is_file() and pathlib.Path(f).suffix in ('.md', '.json', '.yaml', '.yml', '.txt', '.js', '.py', '.svg')]
for p in text_files:
    rel = p.relative_to(ROOT).as_posix()
    s = p.read_text(errors='ignore')
    if rel not in URL_FILES:
        for m in re.findall(r'https?://api\.[a-z0-9.-]+/mcp/server', s):
            errors.append(f'{rel}: MCP 地址只能写在 ' + ' / '.join(URL_FILES) + f'，发现 {m}')
    errors += deny_hits(rel, s)

# 1b. npm 包与 Claude 插件版本号一致（同一份内容两处发布）
pkg_ver = json.loads((ROOT / 'package.json').read_text())['version']
plugin_ver = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())['version']
if pkg_ver != plugin_ver:
    errors.append(f'package.json 版本 {pkg_ver} 与 .claude-plugin/plugin.json 版本 {plugin_ver} 不一致')

# 2. skill 格式：frontmatter 有 name/description，name 与目录名一致，description 不超长
tools = {l.strip() for l in (ROOT / 'scripts/tools.txt').read_text().splitlines() if l.strip() and not l.startswith('#')}
# 形似 tool 名但其实是参数取值的标识（团队统计的 metric 取值）
NON_TOOLS = {'wallet_spend'}
tool_pat = re.compile(r'`((?:outreach|search|get|list|unlock|create|add|remove|check|employee|module|wallet|activity)_[a-z_]+)`')
# WorkBuddy 版 connect 与技能市场入口 skill 也按同样规则检查（名字取自 frontmatter 期望值）
wb_conf = json.loads((ROOT / 'workbuddy/skills.json').read_text())
SKILL_SOURCES = [(p, p.parent.name) for p in sorted((ROOT / 'skills').glob('*/SKILL.md'))]
SKILL_SOURCES += [(ROOT / 'workbuddy/connect.md', 'scrumball-connect'), (ROOT / 'workbuddy/entry.md', wb_conf['entry']['name'])]
for skill, name in SKILL_SOURCES:
    s = skill.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
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

# 4. WorkBuddy 连接器配置（官方规范 open.workbuddy.cn/docs/connector）
wb_mcp = json.loads((ROOT / 'workbuddy/mcp.json').read_text())['mcpServers']
if len(wb_mcp) != 1:
    errors.append('workbuddy/mcp.json 只能配置一个 MCP Server')
for k, v in wb_mcp.items():
    if v.get('type') != 'streamableHttp' or v.get('url') != url:
        errors.append(f'workbuddy/mcp.json 的 {k} 必须是 streamableHttp 且地址与 .mcp.json 一致')
meta = json.loads((ROOT / 'workbuddy/connector-meta.json').read_text())
for k in ('name', 'name_en', 'description', 'description_zh', 'description_en', 'source', 'examples_zh', 'examples_en'):
    if not meta.get(k):
        errors.append(f'workbuddy/connector-meta.json 缺少 {k}')
if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', meta.get('source', '')):
    errors.append('workbuddy/connector-meta.json 的 source 只能用小写字母、数字和连字符')
for k in ('examples_zh', 'examples_en'):
    if not 2 <= len(meta.get(k) or []) <= 5:
        errors.append(f'workbuddy/connector-meta.json 的 {k} 应为 2～5 条')
if meta.get('version') != pkg_ver:
    errors.append(f'workbuddy/connector-meta.json 版本 {meta.get("version")} 与 package.json {pkg_ver} 不一致')
# 用了 examples_* 字段，最低版本必须声明到 4.24.0（官方：低版本客户端会拉到不兼容配置）
def ver(v):
    return tuple(int(x) for x in re.findall(r'\d+', v or '0'))
if ver(meta.get('minWorkbuddyVersion')) < (4, 24, 0):
    errors.append('workbuddy/connector-meta.json 用了 examples_*，minWorkbuddyVersion 不能低于 4.24.0')
skill_names = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
if set(wb_conf['skills']) != skill_names:
    errors.append(f'workbuddy/skills.json 的 skill 列表 {sorted(wb_conf["skills"])} 与 skills/ 目录 {sorted(skill_names)} 不一致')
# 入口 skill 与连接器自带的 skill 同时安装时不能重名
if wb_conf['entry']['name'] in skill_names:
    errors.append('技能市场入口 skill 不能与 skills/ 下的 skill 重名')
for k in ('description_zh', 'description_en', 'display_name', 'display_name_en'):
    for n, info in list(wb_conf['skills'].items()) + [('entry', wb_conf['entry'])]:
        if not info.get(k):
            errors.append(f'workbuddy/skills.json 的 {n} 缺少 {k}')
if not wb_conf.get('author'):
    errors.append('workbuddy/skills.json 缺少 author')

if errors:
    print('\n'.join('FAIL ' + e for e in errors)); sys.exit(1)
print(f'OK：{len(SKILL_SOURCES)} 个 skill（含 WorkBuddy 版 connect 与入口 skill）通过检查，MCP 地址 {url}')
