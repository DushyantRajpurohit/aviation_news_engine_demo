import trafilatura
from bs4 import BeautifulSoup

def extract_article(url):
    html = trafilatura.fetch_url(url)
    if not html:
        return None, None

    # Extract clean article text
    content = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=False
    )

    # Extract headline from <title>
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    headline = title_tag.get_text(strip=True) if title_tag else None

    return headline, content
