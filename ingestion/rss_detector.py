import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

COMMON_RSS_PATHS = [
    "/rss", "/feed", "/rss.xml", "/feed.xml"
]

def auto_detect_rss(website_url):
    for path in COMMON_RSS_PATHS:
        rss_url = urljoin(website_url, path)
        try:
            r = requests.get(rss_url, timeout=5)
            if r.status_code == 200 and "<rss" in r.text.lower():
                return rss_url
        except:
            pass

    try:
        r = requests.get(website_url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all("link", rel="alternate"):
            href = link.get("href", "")
            if "rss" in href.lower():
                return urljoin(website_url, href)
    except:
        pass

    return None