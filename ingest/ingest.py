from xml.dom import minidom
from bs4 import BeautifulSoup as soup4
from urllib.request import urlopen

class Elem:
    def __init__(self, dom):
        self._dom = dom
        for node in dom.childNodes:
            if isinstance(node, minidom.Text): continue
            setattr(self, node.localName.capitalize(), getNodeText(node))


def do_ingest(url:str):
    main_rss = minidom.parse(urlopen(url))
    articles = []
    for elem in dom_tagpath(main_rss, "rss/channel").childNodes:
        if elem.localName == "item":
            el = Elem(elem)
            articles.append((el.Title, el.Link, el.Description))
    return articles

def getNodeText(mainnode):
    # Iterate all Nodes aggregate TEXT_NODE
    nodelist = mainnode.childNodes
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            # ! Recursive
            rc.append(getNodeText(node))
    return '<br/>'.join(rc)

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
    section, top_link, _ = elem
    sub_articles = []

    page = soup4(urlopen(top_link), 'html.parser')
    list_items = [li for li in page.find_all("li") if li.find("blockquote")]
    for top in list_items:
        source = top.find("em")
        a_elem = top.find("a")
        quote = top.find("blockquote")

        if None in [source, a_elem, quote]:
            continue

        link = a_elem['href']
        title = f"{section} / {source.text} : {a_elem.text}"
        description = '\n'.join([p.text for p in quote.find_all("p")])
        
        sub_articles.append((title, link, description))
    return sub_articles

def expand(articles:list[tuple[str,str,str]]):
    new_list = []
    for elem in articles:
        title,link,description = elem

        if title.lower() in ["security leftovers", "today's howtos", "programming leftovers"]:
            # these share the same page format
            items = explode(elem)
            assert len(items), f"Section {title} found no articles! Page format change? // {link}"
            new_list.extend(items)
        elif title.lower() in ["android leftovers", "today in techrights"]:
            # these two have their own distinct formats
            # there's no consistency!
            new_list.append(elem)
        else:
            new_list.append(elem)
    return new_list