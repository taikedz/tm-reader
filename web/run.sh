#!/usr/bin/env bash

HEREDIR="$(dirname "$(realpath "$0")")"

cd "$HEREDIR"

if [[ -z "$*" ]]  || [[ "$1" = "up" ]]; then
    docker compose up -d
elif [[ "$1" = bounce ]]; then
    docker compose down && docker compose up -d
elif [[ "$1" = down ]]; then
    docker compose down
else
    echo "Invalid operation '$1'"
    exit 1
fi
