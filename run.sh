#!/bin/bash
cd "$(dirname "$0")"
python3 backend/app.py &
yarn --cwd frontend/ start &
wait -n
exit $?
