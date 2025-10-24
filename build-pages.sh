#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

mkdir -p web
./run.sh -o web/articles-today.json
./run.sh -l web/articles-today.json -t web/howtos.html howtos
./run.sh -l web/articles-today.json -t web/security.html security
./run.sh -l web/articles-today.json -t web/golang.html golang
./run.sh -l web/articles-today.json -t web/programming.html "programming leftovers"