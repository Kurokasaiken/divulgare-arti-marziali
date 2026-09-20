#!/usr/bin/env python3
"""Run mw-ask.py locally or in a GitHub Codespace based on free RAM.

If free RAM is above the threshold, run locally. If below, run in the
configured Codespace to spare the Mac.
"""
import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path

try:
    import psutil
except ImportError:
    print("[errore] psutil non installato. Esegui: .mw/venv/bin/pip install psutil", file=sys.stderr)
    sys.exit(1)

DEFAULT_CODESPACE = os.environ.get("MW_CODESPACE", "symmetrical-memory-vrgv5x77w5rf695q")
DEFAULT_THRESHOLD_MB = int(os.environ.get("MW_RAM_THRESHOLD_MB", "2048"))
REPO_ROOT = Path(__file__).resolve().parent.parent


def _free_ram_mb() -> int:
    return psutil.virtual_memory().available // (1024 * 1024)


def _workspace_from_prompt(prompt: str) -> str:
    p = prompt.lower()
    if "rpg" in p or "rpgbalancer" in p:
        return "/workspaces/RpgBalancer"
    return "/workspaces/MindWeaver"


def _run_local(provider, model, prompt, system=None, hat=None):
    cmd = [
        str(REPO_ROOT / ".mw" / "venv" / "bin" / "python"),
        "scripts/mw-ask.py",
        "--provider", provider,
        "--model", model,
        "--prompt", prompt,
    ]
    if system:
        cmd += ["--system", system]
    if hat:
        cmd += ["--hat", hat]
    return subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)


def _run_remote(provider, model, prompt, workspace, system=None, hat=None):
    if workspace == "/workspaces/RpgBalancer":
        prompt = f"[Contesto: stai lavorando nel repo {workspace}.] {prompt}"
    quoted = shlex.quote(prompt)
    remote_cmd = f"cd /workspaces/MindWeaver && .mw/venv/bin/python scripts/mw-ask.py --provider {provider} --model {model} --prompt {quoted}"
    if system:
        remote_cmd += f" --system {shlex.quote(system)}"
    if hat:
        remote_cmd += f" --hat {shlex.quote(hat)}"
    return subprocess.run(
        ["gh", "codespace", "ssh", "-c", DEFAULT_CODESPACE, "--", remote_cmd],
        capture_output=True,
        text=True,
    )


def main():
    parser = argparse.ArgumentParser(description="Ask a model locally or in the cloud based on free RAM.")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--system", default=None)
    parser.add_argument("--hat", default=None)
    parser.add_argument("--ram-threshold-mb", type=int, default=DEFAULT_THRESHOLD_MB)
    parser.add_argument("--codespace", default=DEFAULT_CODESPACE)
    args = parser.parse_args()

    free = _free_ram_mb()
    workspace = _workspace_from_prompt(args.prompt)
    print(f"[mw-ask-auto] RAM libera: {free} MB. Soglia: {args.ram_threshold_mb} MB.", file=sys.stderr)

    if free >= args.ram_threshold_mb:
        print("[mw-ask-auto] Eseguo in locale.", file=sys.stderr)
        result = _run_local(args.provider, args.model, args.prompt, args.system, args.hat)
    else:
        print(f"[mw-ask-auto] RAM bassa, eseguo nel Codespace {args.codespace} ({workspace}).", file=sys.stderr)
        result = _run_remote(args.provider, args.model, args.prompt, workspace, args.system, args.hat)

    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
