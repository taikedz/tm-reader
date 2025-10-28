from htmlgen.htmlgen import html_summary_gen

# header suggestions https://blog.jim-nielsen.com/2025/dont-forget-these-html-tags/

HEADER = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Tux Machines {filter_name}</title>
<link rel="stylesheet" href="tuxmachines.css">
</head><body>

<p style="float: left"></p>
<p class="headlink"><a href="../">⬆️(up)</a> - <a href="https://news.tuxmachines.org/" target="_blank">From Tux Machines</a></p>
<p class="styleicon"><a href="/tuxmachines.css">🪶</a></p>
"""

FOOTER = """
</body></html>
"""
