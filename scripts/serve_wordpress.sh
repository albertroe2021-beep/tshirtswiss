#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../wordpress"
echo "Serving /workspaces/Tshirtswiss.ch/wordpress on http://0.0.0.0:8080"
python3 -m http.server 8080 --bind 0.0.0.0
