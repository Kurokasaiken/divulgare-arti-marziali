#!/usr/bin/env bash
set -e

REPO="Kurokasaiken/MindWeaver"

case "$1" in
    start)
        echo "Avvio Codespace..."
        gh codespace create --repo "$REPO" --branch main
        ;;
    stop)
        echo "Arresto Codespaces..."
        gh codespace list --repo "$REPO" --json name --jq '.[].name' | while read name; do
            gh codespace stop --repo "$REPO" "$name"
        done
        ;;
    status)
        echo "Stato Codespaces:"
        gh codespace list --repo "$REPO"
        ;;
    *)
        echo "Uso: $0 {start|stop|status}"
        exit 1
        ;;
esac
