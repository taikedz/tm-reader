# TuxMachines Reader

[TuxMachines's](https://news.tuxmachines.org/) landing page is an eyesore. It also has a number of articles that are themselves lists of articles.

This mini-project aims to

* digest tuxm's main page listing to produce a new, structured listing of articles
* producing a new plain HTML listing for browser viewing
* as well as a RSS feed for news aggregators

## Running

* `./run.sh` runs the script, takes care of ensuring venv dependencies are met.
* `build-pages.sh` builds specific pages I am interested in. Edit to produce your own
* `create-index.sh` creates an index for the main web directory based on the existing pages generated. automatically called by the page builder

## Serving

You can open the files locally.

If you want to run `build-pages.sh` on a cron on a server, you can then serve using docker and docker compose. Use `./web/run.sh up` to stand up the server on port 8080. Edit the `docker-compose.yaml` to change the exposed port.
