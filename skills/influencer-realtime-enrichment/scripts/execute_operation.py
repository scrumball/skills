#!/usr/bin/env python3
"""Self-contained operation runner for this skill."""
from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict

OPERATIONS_PATH = Path(__file__).resolve().parents[1] / "references" / "operations.json"
SKILL_ROOT = Path(__file__).resolve().parents[1]


def load_operations() -> Dict[str, Dict[str, Any]]:
    with OPERATIONS_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_json_arg(raw: str | None, label: str) -> Dict[str, Any]:
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON for {label}: {e}") from e
    if not isinstance(data, dict):
        raise ValueError(f"{label} must be a JSON object")
    return data


def apply_path_params(path: str, path_params: Dict[str, Any]) -> str:
    rendered = path
    for k, v in path_params.items():
        rendered = rendered.replace("{" + k + "}", str(v))
    return rendered


def validate_required(required: list[str], payload: Dict[str, Any], label: str) -> None:
    missing = [k for k in required if k not in payload or payload[k] in (None, "")]
    if missing:
        raise ValueError(f"Missing required {label}: {', '.join(missing)}")


def validate_required_any(required_any: list[str], payload: Dict[str, Any], label: str) -> None:
    if not required_any:
        return
    present = any(k in payload and payload[k] not in (None, "") for k in required_any)
    if not present:
        raise ValueError(f"Missing required {label}: at least one of {', '.join(required_any)}")


def auth_header_value(api_key: str) -> str:
    prefix = os.getenv("SCRUMBALL_AUTH_PREFIX", "").strip()
    return f"{prefix} {api_key}" if prefix else api_key


def load_env_file(path: Path) -> None:
    if not path.exists() or not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        key = k.strip()
        if not key:
            continue
        val = v.strip().strip('"').strip("'")
        # Do not override already-exported env
        if key not in os.environ:
            os.environ[key] = val


def resolve_and_load_env(env_file_arg: str | None) -> None:
    candidates = []
    if env_file_arg:
        candidates.append(Path(env_file_arg).expanduser())
    elif os.getenv("SCRUMBALL_ENV_FILE"):
        candidates.append(Path(os.getenv("SCRUMBALL_ENV_FILE", "")).expanduser())
    else:
        # deterministic fallback for installed single-skill usage
        candidates.append(Path.cwd() / ".env")
        candidates.append(SKILL_ROOT / ".env")

    for p in candidates:
        if p.exists() and p.is_file():
            load_env_file(p)
            break


def call_operation(op: Dict[str, Any], query: Dict[str, Any], body: Dict[str, Any], headers: Dict[str, Any], path_params: Dict[str, Any]) -> Dict[str, Any]:
    base_url = os.getenv("SCRUMBALL_BASE_URL", "").strip()
    api_key = os.getenv("SCRUMBALL_API_KEY", "").strip()
    timeout = int(os.getenv("SCRUMBALL_TIMEOUT_SECONDS", "30"))

    if not base_url:
        raise ValueError("SCRUMBALL_BASE_URL is required")
    if not api_key:
        raise ValueError("SCRUMBALL_API_KEY is required")

    validate_required(op.get("required_query", []), query, "query parameters")
    validate_required_any(op.get("required_any_query", []), query, "query parameters")
    validate_required(op.get("required_path", []), path_params, "path parameters")
    validate_required(op.get("required_body", []), body, "body fields")

    url = base_url.rstrip("/") + apply_path_params(op["path"], path_params)
    if query:
        q = {k: v for k, v in query.items() if v is not None}
        if q:
            url += "?" + urllib.parse.urlencode(q, doseq=True)

    req_headers = {
        "authorization": auth_header_value(api_key),
        "accept": "application/json",
    }
    req_headers.update(op.get("default_headers", {}))
    req_headers.update({k: str(v) for k, v in headers.items()})

    data = None
    if body:
        req_headers["content-type"] = "application/json"
        data = json.dumps(body).encode("utf-8")

    req = urllib.request.Request(url=url, method=op["method"], headers=req_headers, data=data)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
            try:
                payload = json.loads(raw) if raw else None
            except json.JSONDecodeError:
                payload = raw
            return {"ok": True, "status": resp.getcode(), "url": url, "data": payload}
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace") if e.fp else ""
        try:
            payload = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            payload = raw
        return {"ok": False, "status": e.code, "url": url, "error": payload}
    except urllib.error.URLError as e:
        raise ValueError(f"Network error: {e}") from e


def main() -> int:
    parser = argparse.ArgumentParser(description="Run operations for this skill")
    parser.add_argument("--env-file", help="Optional .env file path; if omitted, auto-tries ./.env then <skill-root>/.env")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list")
    p_list.add_argument("--tag")

    p_call = sub.add_parser("call")
    p_call.add_argument("--operation", required=True)
    p_call.add_argument("--query")
    p_call.add_argument("--body")
    p_call.add_argument("--headers")
    p_call.add_argument("--path-params")

    args = parser.parse_args()
    resolve_and_load_env(args.env_file)
    ops = load_operations()

    if args.cmd == "list":
        rows = [(oid, meta) for oid, meta in ops.items()]
        rows.sort(key=lambda x: (x[1]["path"], x[1]["method"]))
        if args.tag:
            rows = [x for x in rows if args.tag in (x[1].get("tags") or [])]
        for oid, meta in rows:
            print(f"{oid}\t{meta['method']}\t{meta['path']}\t{','.join(meta.get('tags') or [])}\t{meta.get('summary','')}")
        print(f"TOTAL\t{len(rows)}")
        return 0

    try:
        op = ops[args.operation]
    except KeyError:
        print(f"ERROR: Unknown operationId: {args.operation}")
        return 1

    try:
        query = parse_json_arg(args.query, "--query")
        body = parse_json_arg(args.body, "--body")
        headers = parse_json_arg(args.headers, "--headers")
        path_params = parse_json_arg(args.path_params, "--path-params")
        res = call_operation(op, query, body, headers, path_params)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0 if res.get("ok") else 2
    except ValueError as e:
        print(f"ERROR: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
