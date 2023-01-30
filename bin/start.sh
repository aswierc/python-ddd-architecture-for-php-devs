#!/bin/bash

set -Eeuo pipefail

export PATH="$PATH:./venv/bin"

uvicorn app:app --host 127.0.0.1 --port 8080 --reload

