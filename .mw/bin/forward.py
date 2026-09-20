#!/usr/bin/env python3
"""Proxy Mind Weaver scripts into the project workspace."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MW = (ROOT / Path("../mind-weaver")).resolve()

SCRIPT = Path(sys.argv[0]).name
PYTHON = MW / ".mw" / "venv" / "bin" / "python"
TARGET = MW / "scripts" / SCRIPT

cmd = [str(PYTHON), str(TARGET)] + sys.argv[1:]
result = subprocess.run(cmd, cwd=str(ROOT))
sys.exit(result.returncode)
