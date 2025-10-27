#!/usr/bin/env python3

import argparse
import datetime
import json
import re

import ingest
import htmlgen



MAIN_FEED_URL="https://news.tuxmachines.org/feed.xml"

def filter_select(articles, filter_list):
    retained_articles = []

    for artic in articles:
        title, olink, description, pubdate = artic
        lo_t = title.lower()
        lo_d = description.lower()
        retain = False

        if filter_list:
            for findtext in filter_list:
                if findtext.startswith("="):
                    findtext = findtext[1:]
                    if findtext in title or findtext in description:
                        retain = True
                        break
                elif findtext.startswith("~"):
                    findtext = findtext[1:]
                    if re.findall(findtext, title) or re.findall(findtext, description):
                        retain = True
                        break
                else:
                    findtext = findtext.lower()
                    if findtext in lo_t or findtext in lo_d:
                        retain = True
                        break
            if not retain:
                continue

        if not artic in retained_articles:
            # FIXME - this is a shim to remove duplicates
            # but duplicates should not be appearing in the first place
            retained_articles.append(artic)
    return retained_articles


def cli_summary(articles):
    count = 0

    for artic in articles:
        title, link, description, pubdate = artic

        count += 1

        print(f"""{title}
        {pubdate}
        {link}
        {description}
        """)
        print("===")
    print(f"--> {count} articles.")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", "-t", help="Generate HTML into given file", default=None)
    parser.add_argument("--cli", "-c", help="Generate CLI output", action="store_true")
    parser.add_argument("--save", "-o", help="Save as JSON")
    parser.add_argument("--load", "-l", help="Load from JSON instead of Web")
    parser.add_argument("filters", nargs="*", help="CLI filters - match articles containing term in title or description (case insensitive). Prefix with '=' for case-sensitive. Prefix with '~' for a regex")

    args = parser.parse_args()
    assert args.save or args.html or args.cli, "Specify -o, -c or -t to generate output. Specify -h for help."

    return args


def load_articles(filepath):
    with open(filepath) as fh:
        return json.load(fh)


def save_articles(articles, filepath):
    with open(filepath, 'w') as fh:
        json.dump(articles, fh)


def main():
    args = parse_args()
    try:
        if args.load:
            articles = load_articles(args.load)
        else:
            articles = ingest.do_ingest(MAIN_FEED_URL)
            articles = ingest.expand(articles)

        if args.save:
            save_articles(articles, args.save)

        articles = filter_select(articles, args.filters)
        filter_name = f": {', '.join(args.filters)}" if args.filters else ""

        if args.html:
            with open(args.html, 'w') as fh:
                fh.write(htmlgen.HEADER.format(filter_name=filter_name))
                fh.write(f'<p class="gendate">Generated on {datetime.datetime.now()}</p>')

                for blob in htmlgen.html_summary_gen(articles):
                    fh.write(blob)

                fh.write(htmlgen.FOOTER)

        if args.cli:
            cli_summary(articles)

    except AssertionError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
