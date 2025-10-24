#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

mkdir -p web
( set -x
./run.sh -o web/articles-today.json
rm web/htdocs/*.html

# Use a number on the page filename to determine its order inthe index

# Process everything
./run.sh -l web/articles-today.json -t web/htdocs/01-tuxmachines.html

# Filtered pages
./run.sh -l web/articles-today.json -t web/htdocs/02-security.html      security
./run.sh -l web/articles-today.json -t web/htdocs/03-howtos.html        howtos
./run.sh -l web/articles-today.json -t web/htdocs/04-programming.html   golang zig ziglang
./run.sh -l web/articles-today.json -t web/htdocs/05-programming-leftovers.html   "programming leftovers"
./run.sh -l web/articles-today.json -t web/htdocs/06-gaming.html        "video game" "gaming"
)

bash create-index.sh