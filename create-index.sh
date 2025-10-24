#!/usr/bin/env bash

HEREDIR="$(dirname "$(realpath "$0")")"
cd "$HEREDIR"

indexf="web/htdocs/index.htm"
echo > "$indexf"
addline() { echo "$*" >> "$indexf"; }

addline '<html><head><title>Tux Machines Sumaries</title>'
addline '<link rel="stylesheet" href="tuxmachines.css"></head><body>'
addline '<ul>'

for page in web/htdocs/*.html; do
    shortname="$(grep -P "<title>Tux Machines : .+</title>" "$page"|sed -r -e 's/^.+?Machines : //' -e 's|</title>||')"
    addline "<li class="pagelink"><a href=\"$(basename "$page")\">${shortname:-All}</a></li>"
done

addline "</ul></body></html>"