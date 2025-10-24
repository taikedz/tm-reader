#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

mkdir -p web
( set -x
./run.sh -o web/articles-today.json
./run.sh -l web/articles-today.json -t web/htdocs/tuxmachines.html
./run.sh -l web/articles-today.json -t web/htdocs/howtos.html howtos
./run.sh -l web/articles-today.json -t web/htdocs/security.html security
./run.sh -l web/articles-today.json -t web/htdocs/golang.html golang
./run.sh -l web/articles-today.json -t web/htdocs/programming.html "programming leftovers"
)

bash create-index.sh