#!/usr/bin/env python3
"""Local state and workspace mapping for the Telegram bridge (PLAN-040).

Authorization and per-chat configuration live in:
    .mw/telegram-state/authorized-chats.yaml

Per-chat state snapshots live in:
    .mw/telegram-state/<chat_id>.yaml

Copy `tools/authorized-chats.yaml.example` to
`.mw/telegram-state/authorized-chats.yaml` and fill your `chat_id`.
"""
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = ROOT / ".mw" / "telegram-state"

WORKSPACE_ALIASES = {
    "rpgbalancer": str(ROOT.parent / "RpgBalancer"),
    "rpg": str(ROOT.parent / "RpgBalancer"),
    "rpg balancer": str(ROOT.parent / "RpgBalancer"),
    "mindweaver": str(ROOT),
    "mind weaver": str(ROOT),
    "mind": str(ROOT),
    "weaver": str(ROOT),
}
AUTH_FILE = STATE_DIR / "authorized-chats.yaml"


_STATE_DIR_ENSURED = False


def _ensure_state_dir():
    global _STATE_DIR_ENSURED
    if not _STATE_DIR_ENSURED:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        _STATE_DIR_ENSURED = True


def _load_yaml(path: Path, default=None):
    _ensure_state_dir()
    if not path.exists():
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or default
    except Exception:
        return default


def _save_yaml(path: Path, data):
    _ensure_state_dir()
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def _load_authorized():
    return _load_yaml(AUTH_FILE, {"chats": {}})


def _state_path(chat_id):
    _ensure_state_dir()
    return STATE_DIR / f"{chat_id}.yaml"


def is_authorized(chat_id):
    cfg = _load_authorized()
    return str(chat_id) in cfg.get("chats", {})


def get_chat_config(chat_id):
    cfg = _load_authorized()
    return cfg.get("chats", {}).get(str(chat_id), {}) or {}


def _resolve_workspace(workspace: str) -> Path:
    if workspace.startswith("$MW_HOME"):
        base = os.environ.get("MW_HOME")
        if base is None:
            base = str(ROOT)
        rest = workspace[len("$MW_HOME"):]
        return Path(base + rest).resolve()
    return Path(workspace).expanduser().resolve()


def get_workspace(chat_id) -> Path:
    cfg = get_chat_config(chat_id)
    return _resolve_workspace(cfg.get("workspace", str(ROOT)))


def resolve_workspace(chat_id, text: str) -> Path:
    """Resolve workspace from message text, falling back to chat default."""
    t = text.lower()
    for alias, ws in WORKSPACE_ALIASES.items():
        if alias in t:
            return _resolve_workspace(ws)
    return get_workspace(chat_id)


def load_state(chat_id):
    default = {
        "state": "idle",
        "clarification": [],
        "pending_plan": None,
        "pending_plan_id": None,
    }
    return _load_yaml(_state_path(chat_id), default)


def save_state(chat_id, state):
    _save_yaml(_state_path(chat_id), state)


def set_state(chat_id, new_state, **fields):
    state = load_state(chat_id)
    state["state"] = new_state
    for k, v in fields.items():
        if v is not None:
            state[k] = v
    save_state(chat_id, state)
    return state


HISTORY_MAX_TURNS = 10


def history_path(chat_id):
    _ensure_state_dir()
    return STATE_DIR / f"{chat_id}-history.yaml"


def load_history(chat_id):
    default = []
    data = _load_yaml(history_path(chat_id), default)
    if not isinstance(data, list):
        return default
    return data


def save_history(chat_id, history):
    _save_yaml(history_path(chat_id), history)


def add_history_turn(chat_id, role, content):
    history = load_history(chat_id)
    from datetime import datetime, timezone  # noqa: E402
    history.append({
        "role": role,
        "content": content,
        "ts": datetime.now(timezone.utc).isoformat(),
    })
    # Keep last N turns (user + assistant = 2 * N entries)
    if len(history) > HISTORY_MAX_TURNS * 2:
        history = history[-HISTORY_MAX_TURNS * 2:]
    save_history(chat_id, history)
    return history


OFFSET_FILE = STATE_DIR / "offset.yaml"


def load_offset() -> int:
    """Load last processed Telegram update offset."""
    if not OFFSET_FILE.exists():
        return 0
    with open(OFFSET_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return int(data.get("offset", 0))


def save_offset(offset: int) -> None:
    _ensure_state_dir()
    with open(OFFSET_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump({"offset": offset}, f)
