#!/usr/bin/env python3
"""Idle shutdown monitor for GitHub Codespaces.

Stops the Codespace after a configurable period of inactivity.
"""
import os
import subprocess
import sys
import time

IDLE_STOP_MIN = int(os.environ.get("MW_IDLE_STOP_MIN", "5"))
SLEEP_SEC = 30
CODESPACE = os.environ.get("CODESPACE_NAME") or os.environ.get("HOSTNAME", "")

ACTIVE_PATTERNS = [
    "telegram-mw-bridge",
    "mw-ask",
    "mw-orchestrate",
    "mw-ask-auto",
    "mw-manual",
    "execution-isolation",
    "execution-strategist",
]


def _has_active_processes() -> bool:
    for name in ACTIVE_PATTERNS:
        try:
            result = subprocess.run(["pgrep", "-f", name], capture_output=True, text=True)
            if result.stdout.strip():
                return True
        except FileNotFoundError:
            return False
    return False


def _stop_codespace() -> None:
    if not CODESPACE:
        print("[idle-stop] CODESPACE_NAME non impostato, non posso fermare.", file=sys.stderr)
        return
    print(f"[idle-stop] Nessuna attività da {IDLE_STOP_MIN} min. Fermo {CODESPACE}.", file=sys.stderr)
    try:
        subprocess.run(["gh", "codespace", "stop", "-c", CODESPACE], capture_output=True, text=True)
    except Exception as e:
        print(f"[idle-stop] Errore stop: {e}", file=sys.stderr)


def main():
    idle_min = 0
    while True:
        time.sleep(SLEEP_SEC)
        if _has_active_processes():
            idle_min = 0
            continue
        idle_min += SLEEP_SEC / 60
        if idle_min >= IDLE_STOP_MIN:
            _stop_codespace()
            sys.exit(0)


if __name__ == "__main__":
    main()
