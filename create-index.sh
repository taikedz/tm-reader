#!/usr/bin/env bash

HEREDIR="$(dirname "$(realpath "$0")")"
cd "$HEREDIR"

indexf="web/htdocs/index.html"
echo > "$indexf"
addline() { echo "$*" >> "$indexf"; }

addline '<!doctype html>'
addline '<html lang="en"><head>'
addline '<meta charset="utf-8">'
addline '<meta name="viewport" content="width=device-width,initial-scale=1.0">'

addline '<title>Tux Machines Sumaries</title>'
addline '<link rel="stylesheet" href="/tuxmachines.css"></head><body>'

addline '<p class="logo-title"><a href="https://news.tuxmachines.org/" target="_blank"><img src="https://news.tuxmachines.org/Images/tuxmachines.logo.svg"></a></p>'
addline '<h1>Tux Machines Views</h1>'

for page in web/htdocs/*.html; do
    if [[ "$(basename "$page")" = index.html ]]; then continue; fi
    shortname="$(grep -P "<title>Tux Machines : .+</title>" "$page"|sed -r -e 's/^.+?Machines : //' -e 's|</title>||')"
    addline "<p class=\"pagelink\"><a href=\"$(basename "$page")\">${shortname:-All}</a></li>"
done

addline "</body></html>"
