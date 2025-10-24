from htmlgen.htmlgen import html_summary_gen

HEADER = """<html>
<head><title>Tux Machines {filter_name}</title>
<meta charset="utf-8">
<link rel="stylesheet" href="tuxmachines.css">
</head><body>
<p style="float: left"></p>
<p class="headlink"><a href="../">(up)</a> - <a href="https://news.tuxmachines.org/" target="_blank">From Tux Machines</a></p>
"""

FOOTER = """
</body></html>
"""