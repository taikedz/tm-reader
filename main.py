from xml.dom import minidom
from urllib.request import urlopen

MAIN_FEED_URL="https://news.tuxmachines.org/feed.xml"

class Elem:
    def __init__(self, dom):
        self._dom = dom
        for node in dom.childNodes:
            if isinstance(node, minidom.Text): continue
            setattr(self, node.localName.capitalize(), getNodeText(node))

def do_ingest():
    main_rss = minidom.parse(urlopen(MAIN_FEED_URL))
    articles = []
    for elem in dom_tagpath(main_rss, "rss/channel").childNodes:
        if elem.localName == "item":
            articles.append(Elem(elem))
    return articles

def getNodeText(mainnode):
    # Iterate all Nodes aggregate TEXT_NODE
    nodelist = mainnode.childNodes
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            # Recursive
            rc.append(getText(node))
    return ''.join(rc)

def dom_tagpath(dom, path):
    tags = path.split("/")
    found = False

    for tag in tags:
        if tag == "": continue
        found = False
        for node in dom.childNodes:
            if node.localName == tag:
                dom = node
                found = True
                break
    return dom if found else None


def explode(elem):
    return [elem]
    sub_articles = []

    pagedom = minidom.parse(urlopen(elem.Link))
    list_items = [li.parentNode for li in pagedom.getElementByTagname("blockquote")]
    print(list_items)
    exit()

def expand(articles:list[Elem]):
    new_list = []
    for elem in articles:
        if not elem.Title.lower() in ["security leftovers", "today's howtos", "programming leftovers"]:
            continue # retain a reduced set for dev FIXME remove this
        if elem.Title == "Security Leftovers":
            new_list.extend(explode(elem))
        else:
            new_list.append(elem)
    return new_list


def cli_summary(elems):
    for e in elems:
        print(f"""{e.Title}
        {e.Description}
        {e.Link}
        """)


def main():
    try:
        articles = do_ingest()
        articles = expand(articles)
        cli_summary(articles)
    except AssertionError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
