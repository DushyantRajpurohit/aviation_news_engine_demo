import feedparser

def discover_latest_article(rss_url):
    feed = feedparser.parse(rss_url)

    if not feed.entries:
        return None

    return feed.entries[0].link