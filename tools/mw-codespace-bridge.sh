#!/usr/bin/env bash
set -e

CODE_NAME="symmetrical-memory-vrgv5x77w5rf695q"

echo "Avvio Codespace..."
gh codespace start -c "$CODE_NAME"

echo "Attesa 30 secondi..."
sleep 30

echo "Clona RpgBalancer se mancante..."
gh codespace ssh -c "$CODE_NAME" -- "
  [ ! -d /workspaces/RpgBalancer ] && git clone https://github.com/Kurokasaiken/RpgBalancer.git /workspaces/RpgBalancer || true
"

echo "Avvio bridge e idle monitor..."
gh codespace ssh -c "$CODE_NAME" -- "
  cd /workspaces/MindWeaver &&
  git pull &&
  sed -i 's|/Users/faustoboni/progetti_personali/mind-weaver|\\$MW_HOME|g' .mw/telegram-state/authorized-chats.yaml 2>/dev/null || true &&
  tmux new -d -s bridge 'export MW_HOME=/workspaces/MindWeaver && .mw/venv/bin/python tools/telegram-mw-bridge.py' &&
  tmux new -d -s idle 'export CODESPACE_NAME=$CODE_NAME && .mw/venv/bin/python tools/mw-codespace-idle-stop.py'
"
