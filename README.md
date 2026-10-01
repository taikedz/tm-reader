# TuxMachines Reader

[TuxMachines's](https://news.tuxmachines.org/) landing page is an eyesore. It also has a number of articles that are themselves lists of articles.

This mini-project aims to

* digest tuxm's main page listing to produce a new, structured listing of articles
* producing a new plain HTML listing for browser viewing
* as well as a RSS feed for news aggregators

## Running

You would run this manually if you just want a one-off pull of current Tux Machines articles

* `./run.sh` runs the script, takes care of ensuring venv dependencies are met.
* `build-pages.sh` builds specific pages I am interested in. Edit to produce your own
* `create-index.sh` creates an index for the main web directory based on the existing pages generated. automatically called by the page builder

```sh
# Download articles once, save to JSON file
./run.sh -o articles.json

# Split out articles into themed pages, re-use the articles list, and save to a HTML file;
#     specify space-separated strings to look for ; use '~' at beginning to use a regex
# These pages can be opened locally
./run.sh -l articles.json -t security.html   security
./run.sh -l articles.json -t gaming.html     SteamOS '~\bGam(e|es|ing)\b'

# Create an index page
./create-index.sh
```

## Serving

You can open the files locally.

Set `build-pages.sh` to run on a cron, e.g.

```crontab
0,30 8-18 * * 1-5 /home/user/git/github.com/taikedz/tm-reader/build-pages.sh
```

Edit `build-pages.sh` to change what the categories will be.

Run `./web/run.sh up` to stand up a NGINX server on port 8080. Edit the `docker-compose.yaml` to change the exposed port.

