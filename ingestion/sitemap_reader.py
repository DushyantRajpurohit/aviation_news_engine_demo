import requests
from xml.etree import ElementTree

def get_latest_from_sitemap(website_url):
    sitemap_url = website_url.rstrip("/") + "/sitemap.xml"
    try:
        r = requests.get(sitemap_url, timeout=5)
        r.raise_for_status()

        root = ElementTree.fromstring(r.content)
        urls = [loc.text for loc in root.findall(".//{*}loc")]
        return urls[-1] if urls else None
    except:
        return None