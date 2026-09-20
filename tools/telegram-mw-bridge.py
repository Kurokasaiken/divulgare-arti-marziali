#!/usr/bin/env python3
"""Telegram bridge for Mind Weaver mobile (PLAN-039).

Usage:
    .mw/venv/bin/python tools/telegram-mw-bridge.py

Environment (from .env or shell):
    TELEGRAM_BOT_TOKEN
    TELEGRAM_USER_ID
    TELEGRAM_MW_PROVIDER (optional; default from .mw/deliberation-config.yaml)
    TELEGRAM_MW_MODEL    (optional; default from .mw/deliberation-config.yaml)
    TELEGRAM_MW_FALLBACK (optional; default from .mw/deliberation-config.yaml)
    TELEGRAM_POLL_INTERVAL (default: 5)

Defaults come from .mw/deliberation-config.yaml (fallbacks section).
.env may override them; explicit values always win.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    import dotenv
except ImportError:
    dotenv = None

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / ".mw" / "deliberation-config.yaml"

sys.path.insert(0, str(ROOT / "tools"))
import telegram_state  # noqa: E402

if dotenv:
    dotenv.load_dotenv(ROOT / ".env")

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_ID = os.environ.get("TELEGRAM_USER_ID")
POLL_INTERVAL = int(os.environ.get("TELEGRAM_POLL_INTERVAL", "5"))

IDLE_MIN = int(os.environ.get("TELEGRAM_IDLE_MIN", "5"))
IDLE_TIMEOUT = IDLE_MIN * 60
_IDLE_TIMER = None
_IDLE_LOCK = threading.Lock()


def _run_power_script(name):
    """Run a power-mode helper script from tools/."""
    script = ROOT / "tools" / name
    if not script.exists():
        print(f"[power] script non trovato: {script}", file=sys.stderr)
        return
    try:
        subprocess.run(
            [str(script)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
    except Exception as e:
        print(f"[power] errore esecuzione {name}: {e}", file=sys.stderr)


def _enter_lowpower():
    _run_power_script("mw-lowpower.sh")


def _enter_workmode():
    global _IDLE_TIMER
    with _IDLE_LOCK:
        if _IDLE_TIMER is not None:
            _IDLE_TIMER.cancel()
            _IDLE_TIMER = None
    _run_power_script("mw-workmode.sh")


def _reschedule_lowpower():
    global _IDLE_TIMER
    with _IDLE_LOCK:
        if _IDLE_TIMER is not None:
            _IDLE_TIMER.cancel()
        if IDLE_TIMEOUT > 0:
            _IDLE_TIMER = threading.Timer(IDLE_TIMEOUT, _enter_lowpower)
            _IDLE_TIMER.daemon = True
            _IDLE_TIMER.start()


def _load_system_prompt(workspace: Path, max_chars: int = 12000):
    """Load a focused system prompt: README, AGENTS head, CANON tail.

    Telegram uses free/weak models. The full AGENTS + CANON + skills is too
    large for their context window, so we trim to the most useful sections.
    """
    parts = [
        (
            "Sei Mind Weaver. Rispondi usando SOLO i documenti di progetto che seguono. "
            "Non usare la tua conoscenza pre-addestrata. Se una risposta non è nel contesto, dillo. "
            "Rispondi in modo conciso."
        )
    ]

    readme = workspace / "README.md"
    if readme.exists():
        parts.append(readme.read_text(encoding="utf-8"))

    agents = workspace / "AGENTS.md"
    if agents.exists():
        text = agents.read_text(encoding="utf-8")
        # Keep first 4000 chars (rules and workflows) and last 2000 (most recent tips)
        head = text[:4000]
        tail = text[-2000:] if len(text) > 6000 else ""
        parts.append("## AGENTS.md\n" + head + ("\n...\n" + tail if tail else ""))

    canon = workspace / "CANON.md"
    if canon.exists():
        text = canon.read_text(encoding="utf-8")
        # Keep last 3000 chars (most recent decisions)
        parts.append("## CANON.md\n" + text[-3000:])

    combined = "\n\n".join(parts)
    if len(combined) > max_chars:
        return combined[:max_chars] + "\n\n[Contesto troncato per rispettare il limite del modello gratuito]"
    return combined


def _load_user_ids():
    raw = ALLOWED_USER_ID
    if raw is None:
        return set()
    ids = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            ids.add(int(part))
        except ValueError:
            pass
    return ids


ALLOWED_USER_IDS = _load_user_ids()


def _load_deliberation_config():
    if not yaml:
        return {}
    try:
        with open(DEFAULT_CONFIG, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def _api_fallbacks(config):
    """Return (provider, model) tuples from the standard API fallback list."""
    out = []
    for item in config.get("fallbacks", []):
        provider = item.get("provider")
        model = item.get("model")
        if provider and model:
            out.append((provider, model))
    return out


_CONFIG = _load_deliberation_config()
_API_FALLBACKS = _api_fallbacks(_CONFIG)

DEFAULT_PROVIDER = os.environ.get("TELEGRAM_MW_PROVIDER") or (
    _API_FALLBACKS[0][0] if _API_FALLBACKS else None
)
DEFAULT_MODEL = os.environ.get("TELEGRAM_MW_MODEL") or (
    _API_FALLBACKS[0][1] if _API_FALLBACKS else None
)

FALLBACK_ENV = os.environ.get("TELEGRAM_MW_FALLBACK", "")
if FALLBACK_ENV:
    FALLBACKS = []
    for item in FALLBACK_ENV.split(";"):
        item = item.strip()
        if not item:
            continue
        if "," in item:
            provider, model = [x.strip() for x in item.split(",", 1)]
            if provider and model:
                FALLBACKS.append((provider, model))
elif _API_FALLBACKS:
    FALLBACKS = _API_FALLBACKS[1:]
else:
    FALLBACKS = []


def _telegram_api(method, **params):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    if params:
        data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
    else:
        req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _send_message(chat_id, text):
    if len(text) > 4000:
        text = text[:3997] + "..."
    return _telegram_api("sendMessage", chat_id=str(chat_id), text=text)


def _ask_mw(prompt, provider=None, model=None, cwd=None, system=None):
    provider = provider or DEFAULT_PROVIDER
    model = model or DEFAULT_MODEL
    cmd = [
        str(ROOT / ".mw" / "venv" / "bin" / "python"),
        str(ROOT / "scripts" / "mw-ask.py"),
        "--provider",
        provider,
        "--model",
        model,
    ]
    if system:
        cmd += ["--system", system]
    cmd += ["--prompt", prompt]
    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd or ROOT),
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode == 0:
            return result.stdout.strip() or "(nessuna risposta)"
        err = result.stderr.strip() or f"exit {result.returncode}"
        return f"[errore mw-ask] {err}"
    except subprocess.TimeoutExpired:
        return "[timeout] mw-ask non ha risposto entro 180s"
    except Exception as e:
        return f"[errore] {e}"


def _ask_mw_with_fallback(prompt, cwd=None, system=None):
    errors = []
    for provider, model in [(DEFAULT_PROVIDER, DEFAULT_MODEL)] + FALLBACKS:
        reply = _ask_mw(prompt, provider, model, cwd=cwd, system=system)
        if not reply.startswith("[errore") and not reply.startswith("[timeout"):
            return reply
        errors.append(f"{provider}/{model}: {reply}")
    return "[tutti i provider hanno falliti]\n" + "\n".join(errors)


# Devin Desktop cliclick integration (PLAN-039/R-128)
_USE_DEVIN_DESKTOP = os.environ.get("TELEGRAM_USE_DEVIN_DESKTOP", "").lower() in ("1", "true", "yes")
_DEVIN_CLICK_X = int(os.environ.get("DEVIN_CLICK_X", "434"))
_DEVIN_CLICK_Y = int(os.environ.get("DEVIN_CLICK_Y", "609"))
_DEVIN_NEW_CHAT_X = int(os.environ.get("DEVIN_NEW_CHAT_X", "135"))
_DEVIN_NEW_CHAT_Y = int(os.environ.get("DEVIN_NEW_CHAT_Y", "90"))
_DEVIN_CHAT_REGION = os.environ.get("DEVIN_CHAT_REGION", "306,112,851,425")
_DEVIN_POLL_INTERVAL = float(os.environ.get("DEVIN_POLL_INTERVAL", "1.0"))
_DEVIN_STABLE_SAMPLES = int(os.environ.get("DEVIN_STABLE_SAMPLES", "3"))
_DEVIN_MAX_WAIT = int(os.environ.get("DEVIN_MAX_WAIT", "120"))
_DEVIN_INITIAL_DELAY = float(os.environ.get("DEVIN_INITIAL_DELAY", "1.5"))


def _devin_to_front():
    subprocess.run(
        ["osascript", "-e", 'tell application "Devin" to activate'],
        capture_output=True,
        check=False,
    )
    time.sleep(0.3)


def _pbcopy(text: str):
    subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)


def _normalize_ocr(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line)


def _ocr_hash(text: str) -> str:
    return hashlib.sha256(_normalize_ocr(text).encode("utf-8")).hexdigest()


def _capture_ocr() -> str:
    shot_path = ROOT / ".mw" / "telegram-state" / "devin_response.png"
    shot_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["screencapture", "-x", "-R", _DEVIN_CHAT_REGION, str(shot_path)],
        check=True,
    )
    try:
        import pytesseract
        from PIL import Image
        return pytesseract.image_to_string(Image.open(shot_path), config="--psm 6").strip() or ""
    except Exception as e:
        print(f"[devin-desktop] OCR error: {e}", file=sys.stderr)
        return ""


def _send_to_devin(message: str):
    _devin_to_front()
    _pbcopy(message)
    time.sleep(0.2)
    # Click input field
    subprocess.run(["/opt/homebrew/bin/cliclick", f"c:{_DEVIN_CLICK_X},{_DEVIN_CLICK_Y}"], check=True)
    time.sleep(0.2)
    # Paste via System Events (more reliable than cliclick modifier combos)
    paste_ok = subprocess.run(
        ["osascript", "-e", 'tell application "System Events" to keystroke "v" using command down'],
        capture_output=True,
    ).returncode == 0
    if not paste_ok:
        # Fallback: use cliclick to type directly
        import shlex
        safe = message.replace('"', '\\"')
        subprocess.run(["/opt/homebrew/bin/cliclick", f't:"{safe}"'], check=True)
    time.sleep(0.2)
    # Press Return via System Events to submit the message
    for code in ["36", "76"]:
        ret = subprocess.run(
            ["osascript", "-e", f'tell application "System Events" to key code {code}'],
            capture_output=True,
        )
        time.sleep(0.1)
    # fallback
    subprocess.run(["/opt/homebrew/bin/cliclick", "kp:return"], check=True)


def _wait_for_stable_ocr(baseline: str) -> str:
    baseline_hash = _ocr_hash(baseline) if baseline else None
    previous_hash = None
    stable = 0
    changed = baseline_hash is None
    latest = ""
    start = time.monotonic()
    time.sleep(_DEVIN_INITIAL_DELAY)
    while True:
        text = _capture_ocr()
        h = _ocr_hash(text)
        latest = text
        if h == previous_hash:
            stable += 1
        else:
            stable = 1
            previous_hash = h
        if baseline_hash and h != baseline_hash:
            changed = True
        if changed and stable >= _DEVIN_STABLE_SAMPLES:
            return latest
        if time.monotonic() - start > _DEVIN_MAX_WAIT:
            return latest
        time.sleep(_DEVIN_POLL_INTERVAL)


def _extract_devin_reply(baseline: str, after: str, user_message: str) -> str:
    base = _normalize_ocr(baseline)
    after = _normalize_ocr(after)
    if not after:
        return ""
    if base and after.startswith(base):
        after = after[len(base):].strip()
    user = _normalize_ocr(user_message)
    if after.startswith(user):
        after = after[len(user):].strip()
    # compact fallback
    compact_after = re.sub(r"\s+", " ", after).strip()
    compact_user = re.sub(r"\s+", " ", user).strip()
    if compact_after.startswith(compact_user):
        after = compact_after[len(compact_user):].strip()
    return after


def _ask_devin_desktop(message: str) -> str:
    """Send a single message to the open Devin Desktop window and read the new reply via OCR."""
    if not os.path.exists("/opt/homebrew/bin/cliclick"):
        return "[errore] cliclick non installato: brew install cliclick"
    try:
        baseline = _capture_ocr()
        _send_to_devin(message)
        after = _wait_for_stable_ocr(baseline)
        reply = _extract_devin_reply(baseline, after, message)
        if not reply:
            return "Devin ha risposto, ma non sono riuscito a estrarre la risposta dallo schermo."
        return reply
    except Exception as e:
        return f"[errore devin-desktop] {e}"


def _start_new_devin_conversation():
    _devin_to_front()
    subprocess.run(["/opt/homebrew/bin/cliclick", f"c:{_DEVIN_NEW_CHAT_X},{_DEVIN_NEW_CHAT_Y}"], check=True)
    time.sleep(1.0)


def _classify_intent(text, system=None):
    """Classify user message into one of: informative, discuss, plan.

    Model-based classification was over-triggering 'plan' on normal questions.
    Use explicit keywords: plan mode only when the user asks for a plan.
    """
    t = text.lower().strip()
    plan_keywords = ["piano", "plan", "crea piano", "voglio un piano", "crea un piano"]
    if any(k in t for k in plan_keywords):
        return "plan"
    if "?" in t or t.startswith("cosa") or t.startswith("come") or t.startswith("dove"):
        return "informative"
    return "discuss"


def _next_plan_number(workspace: Path) -> int:
    """Find the next available PLAN-NNN number in workspace/plans/."""
    plans_dir = workspace / "plans"
    if not plans_dir.exists():
        return 1
    max_n = 0
    for p in plans_dir.glob("PLAN-*-*.md"):
        try:
            n = int(p.stem.split("-")[1])
            max_n = max(max_n, n)
        except (ValueError, IndexError):
            continue
    return max_n + 1


def _plan_filename(workspace: Path, plan_id: str) -> Path:
    return workspace / "plans" / f"{plan_id}-telegram-plan.md"


def _generate_plan(chat_id, state, workspace, system):
    """Generate a plan draft from the stored clarifications."""
    clarifications = state.get("clarification", [])
    history = "\n\n".join(f"- {c}" for c in clarifications)
    prompt = (
        "Sei Mind Weaver. L'utente ha chiesto di creare un piano. "
        "Basandoti sulle informazioni raccolte, scrivi una bozza di piano Mind Weaver "
        "in markdown con frontmatter id, title, status: proposed, created (data odierna). "
        "Le sezioni: Goal, In Scope, NOT In Scope, Tasks, Done, Notes. "
        "Non numerare i task con codici. Scrivi solo il markdown del piano, nient'altro.\n\n"
        f"Informazioni raccolte:\n{history}\n\nPiano:"
    )
    plan_text = _ask_mw_with_fallback(prompt, cwd=workspace, system=system)
    if plan_text.startswith("["):
        return plan_text

    plan_id = f"PLAN-{_next_plan_number(workspace):03d}"
    draft_path = workspace / ".mw" / "telegram-state" / f"{chat_id}-pending-plan.md"
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    # Fix frontmatter id
    plan_text = plan_text.replace("id: PLAN-NNN", f"id: {plan_id}")
    if "id: " not in plan_text.split("---")[1] if "---" in plan_text else True:
        # prepend id if missing
        plan_text = f"---\nid: {plan_id}\nstatus: proposed\ncreated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}\n---\n\n" + plan_text
    draft_path.write_text(plan_text, encoding="utf-8")

    telegram_state.save_state(chat_id, {
        "state": "pending_approval",
        "pending_plan": str(draft_path),
        "pending_plan_id": plan_id,
        "clarification": clarifications,
    })
    return (
        f"Ho preparato una bozza di {plan_id}.\n\n"
        f"Anteprima:\n{plan_text[:1500]}\n\n"
        "Scrivi 'approvo' esatto per battezzarlo."
    )


def _build_conversation_prompt(history, new_text, max_chars=5000):
    """Build a prompt with recent conversation history."""
    header = "Continua la discussione seguendo il contesto.\n\nStorico:"
    body = "\n".join(
        f"{'Utente' if h.get('role') == 'user' else 'Mind Weaver'}: {h.get('content', '')}"
        for h in history
    )
    footer = f"\nUtente: {new_text}\n\nMind Weaver:"
    prompt = f"{header}\n{body}{footer}"
    while len(prompt) > max_chars and history:
        history = history[2:]  # drop oldest turn (user + assistant)
        body = "\n".join(
            f"{'Utente' if h.get('role') == 'user' else 'Mind Weaver'}: {h.get('content', '')}"
            for h in history
        )
        prompt = f"{header}\n{body}{footer}"
    return prompt


def _ask_with_history(chat_id, text, cwd, system):
    if _USE_DEVIN_DESKTOP:
        reply = _ask_devin_desktop(text)
    else:
        history = telegram_state.load_history(chat_id)
        prompt = _build_conversation_prompt(history, text)
        reply = _ask_mw_with_fallback(prompt, cwd=cwd, system=system)
    telegram_state.add_history_turn(chat_id, "user", text)
    telegram_state.add_history_turn(chat_id, "assistant", reply)
    return reply


def _control_intent(text: str) -> str | None:
    """Recognize bridge control commands in natural language."""
    t = text.lower().strip()
    stop_words = ["ferma", "blocca", "stop", "chiudi", "arresta"]
    if any(w in t for w in stop_words):
        return "stop"
    status_words = ["stato", "status"]
    if t in status_words or any(t.startswith(w + " ") for w in status_words):
        return "status"
    remote_words = [
        "remoto", "mobile", "telegram", "bridge", "lavora da",
        "lavorare da", "da remoto", "su git", "il bridge",
    ]
    if any(w in t for w in remote_words):
        return "remote"
    return None


def _route_message(chat_id, text, state, workspace, system, provider, model):
    control = _control_intent(text)
    if control == "stop":
        _send_message(chat_id, "Bridge arrestato. Puoi riavviarlo dal Codespace.")
        sys.exit(0)
    if control == "status":
        return f"Bridge attivo. Provider: {DEFAULT_PROVIDER}/{DEFAULT_MODEL}. Scrivi 'ferma' per fermarlo."
    if control == "remote":
        return "Bridge attivo. Puoi lavorare da remoto su Telegram. Scrivi 'ferma' per fermarlo."

    current = state.get("state", "idle")

    if current == "pending_approval":
        return "In attesa di approvazione. Scrivi 'approvo' esatto per battezzare il piano, oppure scrivi ancora per modificarlo."

    if current in ("idle", "discussing"):
        intent = _classify_intent(text, system=system)
        if intent == "plan":
            telegram_state.set_state(chat_id, "planning_clarify", clarification=[text])
            return (
                "Voglio creare un piano. Descrivi goal, scope, acceptance e vincoli. "
                "Quando hai finito, scrivi 'pronto' per generare la bozza."
            )
        else:
            reply = _ask_with_history(chat_id, text, workspace, system)
            telegram_state.set_state(chat_id, "discussing")
            return reply

    if current == "planning_clarify":
        clarification = list(state.get("clarification", []))
        if text.lower() in ("pronto", "basta", "fatto", "procedi"):
            return _generate_plan(chat_id, state, workspace, system)
        clarification.append(text)
        telegram_state.set_state(chat_id, "planning_clarify", clarification=clarification)
        return "Ok. Altro dettaglio, o scrivi 'pronto' per generare la bozza."

    # fallback
    return _ask_mw_with_fallback(text, cwd=workspace, system=system)


EXECUTION_CONTRACT_REQUIRED_FIELDS = {
    "authorized_actions",
    "forbidden_actions",
    "target_branch",
    "max_cost_usd",
    "max_duration_min",
    "requires_test_pass",
    "on_failure",
    "plan_version",
    "idempotent",
}


def _get_file_commit_sha(path: Path, workspace: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", str(path)],
            cwd=str(workspace),
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _load_execution_contract(plan_path: Path):
    if not yaml:
        return None, "pyyaml non disponibile"
    try:
        text = plan_path.read_text(encoding="utf-8")
    except Exception as e:
        return None, f"impossibile leggere il piano: {e}"
    if not text.startswith("---"):
        return None, "frontmatter mancante"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "frontmatter non valido"
    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except Exception as e:
        return None, f"frontmatter non valido: {e}"
    contract = frontmatter.get("execution_contract")
    if not contract:
        return None, "nessun execution_contract nel frontmatter"
    return contract, None


def _validate_execution_contract(contract: dict):
    missing = EXECUTION_CONTRACT_REQUIRED_FIELDS - set(contract.keys())
    if missing:
        return False, f"campi mancanti: {', '.join(sorted(missing))}"
    if not isinstance(contract["authorized_actions"], list):
        return False, "authorized_actions deve essere una lista"
    if not isinstance(contract["forbidden_actions"], list):
        return False, "forbidden_actions deve essere una lista"
    return True, None


def _run_lock_path(workspace: Path, plan_id: str, sha: str) -> Path:
    runs_dir = workspace / ".mw" / "telegram-state" / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    return runs_dir / f"{plan_id}-{sha}.lock"


def _is_lock_stale(lock_path: Path, max_age_min: int = 35):
    if not lock_path.exists():
        return True
    mtime = lock_path.stat().st_mtime
    age = time.time() - mtime
    return age > max_age_min * 60


def _acquire_run_lock(workspace: Path, plan_id: str, sha: str, max_age_min: int = 35):
    lock = _run_lock_path(workspace, plan_id, sha)
    if lock.exists() and not _is_lock_stale(lock, max_age_min):
        return False, f"Esecuzione già in corso per {plan_id} @ {sha}."
    lock.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")
    return True, None


def _release_run_lock(workspace: Path, plan_id: str, sha: str):
    _run_lock_path(workspace, plan_id, sha).unlink(missing_ok=True)


def _handle_approval(chat_id, state, workspace):
    if state.get("state") != "pending_approval":
        return "Non c'è nessun piano in attesa di approvazione."
    pending_path = state.get("pending_plan")
    plan_id = state.get("pending_plan_id") or f"PLAN-{_next_plan_number(workspace):03d}"
    if not pending_path or not Path(pending_path).exists():
        return "Bozza non trovata. Non posso battezzare."

    src = Path(pending_path)
    dst = _plan_filename(workspace, plan_id)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    # commit
    try:
        subprocess.run(["git", "add", str(dst)], cwd=str(workspace), check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"Baptize {plan_id} from Telegram"],
            cwd=str(workspace),
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        return f"Errore nel commit: {e.stderr.decode('utf-8', errors='replace') if e.stderr else str(e)}"

    # T-008: execution contract validation
    contract, err = _load_execution_contract(dst)
    if err:
        telegram_state.set_state(chat_id, "idle", pending_plan=None, pending_plan_id=None)
        return f"{plan_id} battezzato e committato in {dst}.\n\n⚠️ Esecuzione non attivata: {err}."

    ok, err = _validate_execution_contract(contract)
    if not ok:
        telegram_state.set_state(chat_id, "idle", pending_plan=None, pending_plan_id=None)
        return f"{plan_id} battezzato e committato in {dst}.\n\n⚠️ Esecuzione non attivata: contratto non valido ({err})."

    sha = _get_file_commit_sha(dst, workspace)
    if sha and contract.get("plan_version") != sha:
        telegram_state.set_state(chat_id, "idle", pending_plan=None, pending_plan_id=None)
        return (
            f"{plan_id} battezzato e committato in {dst}.\n\n"
            f"⚠️ Esecuzione non attivata: plan_version ({contract.get('plan_version')}) "
            f"non corrisponde al commit SHA ({sha})."
        )

    # T-009: lock/idempotenza
    max_duration = int(contract.get("max_duration_min", 30))
    acquired, lock_err = _acquire_run_lock(workspace, plan_id, sha or "n/a", max_age_min=max_duration + 5)
    if not acquired:
        telegram_state.set_state(chat_id, "idle", pending_plan=None, pending_plan_id=None)
        return (
            f"{plan_id} battezzato e committato in {dst}.\n\n"
            f"⚠️ Esecuzione non attivata: {lock_err}"
        )

    telegram_state.set_state(
        chat_id,
        "idle",
        pending_plan=None,
        pending_plan_id=None,
        approved_plan=str(dst),
        approved_plan_commit=sha,
    )
    return (
        f"{plan_id} battezzato e committato in {dst}.\n\n"
        f"✅ Execution Contract valido. Lock acquisito. "
        f"Esecuzione automatica disponibile (plan_version: {sha or 'n/d'})."
    )


def _handle_message(update):
    msg = update.get("message", {})
    chat_id = msg.get("chat", {}).get("id")
    user_id = msg.get("from", {}).get("id")
    text = msg.get("text", "")

    if not text or not chat_id:
        return
    if user_id not in ALLOWED_USER_IDS:
        print(f"[auth] user_id {user_id} non autorizzato", file=sys.stderr)
        return
    if not telegram_state.is_authorized(chat_id):
        _send_message(chat_id, "Chat non autorizzata. Configura .mw/telegram-state/authorized-chats.yaml")
        return

    text = text.strip()

    if _USE_DEVIN_DESKTOP and text.lower() in ("new", "nuova", "/new", "/nuova"):
        _start_new_devin_conversation()
        _send_message(chat_id, "Nuova conversazione Devin avviata.")
        return

    _enter_workmode()
    shutdown_words = {
        w.strip().lower() for w in os.environ.get("TELEGRAM_SHUTDOWN_WORDS", "").split(",") if w.strip()
    }
    if shutdown_words and text.lower() in shutdown_words:
        _send_message(
            chat_id,
            "Chiudo la sessione mobile. Il Mac si spegnerà dopo 1 minuto di inattività, salvo nuovi interventi.",
        )
        flag = ROOT / ".mw" / "telegram-state" / "shutdown-requested"
        flag.parent.mkdir(parents=True, exist_ok=True)
        flag.touch()
        sys.exit(0)

    cfg = telegram_state.get_chat_config(chat_id) or {}
    workspace = telegram_state.resolve_workspace(chat_id, text)
    state = telegram_state.load_state(chat_id)
    provider = cfg.get("default_provider") or DEFAULT_PROVIDER
    model = cfg.get("default_model") or DEFAULT_MODEL
    system = _load_system_prompt(workspace)

    if text in ("/start", "/help"):
        fallback_list = ", ".join(f"{p}/{m}" for p, m in FALLBACKS) or "nessuno"
        reply = (
            f"Ciao. Scrivi un messaggio e Mind Weaver risponderà usando "
            f"{provider}/{model}. "
            f"Workspace: {workspace}. "
            f"Fallback: {fallback_list}. "
            "Comandi: /help, /start."
        )
    elif text.lower() == "approvo":
        reply = _handle_approval(chat_id, state, workspace)
    else:
        reply = _route_message(chat_id, text, state, workspace, system, provider, model)

    _send_message(chat_id, reply)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--devin-desktop", action="store_true", help="Inoltra i messaggi a Devin Desktop invece di mw-ask")
    args = parser.parse_args()
    global _USE_DEVIN_DESKTOP
    if args.devin_desktop:
        _USE_DEVIN_DESKTOP = True

    if not BOT_TOKEN:
        print("TELEGRAM_BOT_TOKEN mancante", file=sys.stderr)
        sys.exit(1)
    if not ALLOWED_USER_ID:
        print("TELEGRAM_USER_ID mancante o non valido", file=sys.stderr)
        sys.exit(1)
    if not _USE_DEVIN_DESKTOP and (not DEFAULT_PROVIDER or not DEFAULT_MODEL):
        print(
            "TELEGRAM_MW_PROVIDER/TELEGRAM_MW_MODEL mancanti "
            "e nessun default in .mw/deliberation-config.yaml",
            file=sys.stderr,
        )
        sys.exit(1)

    offset = telegram_state.load_offset()
    print(f"Bridge avviato. Provider: {DEFAULT_PROVIDER}/{DEFAULT_MODEL}")
    _reschedule_lowpower()
    while True:
        resp = _telegram_api("getUpdates", offset=offset, limit=10)
        if not resp.get("ok"):
            print(f"Errore polling: {resp.get('error', resp)}", file=sys.stderr)
            time.sleep(POLL_INTERVAL)
            continue

        for update in resp.get("result", []):
            offset = max(offset, update.get("update_id", 0) + 1)
            telegram_state.save_offset(offset)
            try:
                _handle_message(update)
            except Exception as e:
                print(f"[ERR] update {update.get('update_id')}: {e}", file=sys.stderr)
            _reschedule_lowpower()

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()