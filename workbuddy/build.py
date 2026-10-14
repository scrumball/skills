#!/usr/bin/env python3
"""生成 WorkBuddy 上架包：连接器包（mcp.json + skills）与技能市场入口 skill，输出到 dist/workbuddy/（不进 git）。

skill 只有 skills/ 一份源文件；这里复制后按 WorkBuddy 要求在 frontmatter 补 display_name / description_zh /
description_en / version / author，并把 scrumball-connect 换成 WorkBuddy 版（connect.md）。

用法：python3 workbuddy/build.py [--icon 图标路径]
  图标默认取 workbuddy/icon.svg|png|jpg；没有图标直接失败（官方必填）。
"""
import argparse, json, pathlib, re, shutil, subprocess, sys, zipfile

WB = pathlib.Path(__file__).resolve().parent
ROOT = WB.parent
OUT = ROOT / 'dist' / 'workbuddy'


def fail(msg):
    print('FAIL ' + msg); sys.exit(1)


def inject(skill_md: str, fields: dict) -> str:
    """在 frontmatter 末尾追加 WorkBuddy 字段；值一律 JSON 双引号（合法 YAML，避免冒号等字符出错）。"""
    m = re.match(r'^---\n(.*?)\n---\n', skill_md, re.S)
    if not m:
        fail('SKILL.md 缺少 frontmatter')
    # compatibility 是 Agent Skills 通用字段，不在 WorkBuddy 字段表里，打包时去掉
    head = re.sub(r'^compatibility:.*\n?', '', m.group(1), flags=re.M).rstrip('\n')
    existing = set(re.findall(r'^(\w[\w-]*):', head, re.M))
    clash = existing & set(fields)
    if clash:
        fail(f'源 SKILL.md 已有 WorkBuddy 字段 {sorted(clash)}，应只在打包时注入')
    extra = '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fields.items())
    return f'---\n{head}\n{extra}\n---\n' + skill_md[m.end():]


def zip_dir(src: pathlib.Path, dest: pathlib.Path):
    """zip 内保留顶层目录（与技能包 {skill-name}/SKILL.md 结构一致）；官方未写明连接器 zip 根目录，入驻后核对。"""
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob('*')):
            if p.is_file() and p.name != '.DS_Store':
                z.write(p, p.relative_to(src.parent).as_posix())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--icon')
    args = ap.parse_args()

    # 先跑全仓检查（地址一致、禁用词、tool 名、WorkBuddy 配置），不通过不打包
    if subprocess.run([sys.executable, str(ROOT / 'scripts/check.py')]).returncode != 0:
        fail('scripts/check.py 未通过')

    icon = pathlib.Path(args.icon) if args.icon else next((WB / f'icon.{e}' for e in ('svg', 'png', 'jpg') if (WB / f'icon.{e}').exists()), None)
    if not icon or not icon.exists():
        fail('缺少图标：放 workbuddy/icon.svg（或 64×64 透明 png/jpg），或用 --icon 指定')
    if icon.suffix.lower() not in ('.svg', '.png', '.jpg'):
        fail('图标只能是 svg / png / jpg')

    meta = json.loads((WB / 'connector-meta.json').read_text())
    conf = json.loads((WB / 'skills.json').read_text())
    version, author = meta['version'], conf['author']

    shutil.rmtree(OUT, ignore_errors=True)

    # 连接器包
    conn = OUT / 'connector' / meta['source']
    (conn / 'skills').mkdir(parents=True)
    shutil.copy(WB / 'connector-meta.json', conn / 'connector-meta.json')
    shutil.copy(WB / 'mcp.json', conn / 'mcp.json')
    shutil.copy(icon, conn / f'icon{icon.suffix.lower()}')
    for src in sorted((ROOT / 'skills').glob('*/SKILL.md')):
        name = src.parent.name
        info = conf['skills'].get(name) or fail(f'workbuddy/skills.json 缺少 {name} 的中英文介绍')
        body = (WB / 'connect.md').read_text() if name == 'scrumball-connect' else src.read_text()
        # 连接器版 connect 里的说明注释只给维护者看，不打进包
        body = re.sub(r'\n<!--.*?-->\n', '\n', body, flags=re.S)
        dest = conn / 'skills' / name
        shutil.copytree(src.parent, dest)
        (dest / 'SKILL.md').write_text(inject(body, {
            'display_name': info['display_name'], 'display_name_en': info['display_name_en'],
            'description_zh': info['description_zh'], 'description_en': info['description_en'],
            'version': version, 'author': author}))
    zip_dir(conn, OUT / f'{meta["source"]}-connector-{version}.zip')

    # 技能市场入口 skill
    entry = conf['entry']
    ent = OUT / 'skill-market' / entry['name']
    ent.mkdir(parents=True)
    body = re.sub(r'\n<!--.*?-->\n', '\n', (WB / 'entry.md').read_text(), flags=re.S)
    (ent / 'SKILL.md').write_text(inject(body, {
        'display_name': entry['display_name'], 'display_name_en': entry['display_name_en'],
        'description_zh': entry['description_zh'], 'description_en': entry['description_en'],
        'version': version, 'author': author}))
    zip_dir(ent, OUT / f'{entry["name"]}-{version}.zip')

    # 产物再扫一遍禁用词：check.py 不扫 dist/，图标 svg 常带导出工具写入的文件名、本地路径
    if subprocess.run([sys.executable, str(ROOT / 'scripts/check.py'), '--scan-dir', str(OUT)]).returncode != 0:
        shutil.rmtree(OUT, ignore_errors=True)
        fail('打包产物里出现禁用词，已删除 dist/workbuddy/')

    for z in sorted(OUT.glob('*.zip')):
        print(f'OK {z.relative_to(ROOT)}')
        for n in zipfile.ZipFile(z).namelist():
            print(f'   {n}')


if __name__ == '__main__':
    main()
