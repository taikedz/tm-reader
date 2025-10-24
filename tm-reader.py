#!/usr/bin/env python3

import argparse
import json

import ingest
import htmlgen

def filter_select(articles, filter_list):
    filter_list = [f.lower() for f in filter_list]
    retained_articles = []

    for e in articles:
        title, _, description = e
        lo_t = title.lower()
        lo_d = description.lower()
        retain = True

        for findtext in filter_list:
            if not ( findtext in lo_t or findtext in lo_d ):
                retain = False
                break
        if not retain:
            continue

        if not e in retained_articles:
            # FIXME - this is a shim to remove duplicates
            # but duplicates should not be appearing in the first place
            retained_articles.append(e)
    return retained_articles


def cli_summary(articles):
    count = 0

    for e in articles:
        title, link, description = e

        count += 1

        print(f"""{title}
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
    parser.add_argument("filters", nargs="*", help="CLI filters - match articles containing term in title or description")
    return parser.parse_args()


def load_articles(filepath):
    with open(filepath) as fh:
        return json.load(fh)


def save_articles(articles, filepath):
    with open(filepath, 'w') as fh:
        json.dump(articles, fh)


def main():
    args = parse_args()
    try:
        assert args.save or args.html or args.cli, "Specify -o, -c or -t to generate output. Specify -h for help."

        if args.load:
            articles = load_articles(args.load)
        else:
            articles = ingest.do_ingest()
            articles = ingest.expand(articles)

        if args.save:
            save_articles(articles, args.save)

        articles = filter_select(articles, args.filters)
        filter_name = ""
        if args.filters:
            filter_name = f": {', '.join(args.filters)}"

        if args.html:
            with open(args.html, 'w') as fh:
                fh.write(htmlgen.HEADER.format(filter_name=filter_name))
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
