from bs4 import BeautifulSoup
import trafilatura
import warnings
from bs4 import XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def extract_images(url, limit=1):
    html = trafilatura.fetch_url(url)
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    images = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        # 🚫 Skip inline/base64 images
        if src.startswith("data:"):
            continue

        # 🚫 Skip icons/logos/svg
        if any(x in src.lower() for x in ["logo", "icon", ".svg"]):
            continue

        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = url.rstrip("/") + src

        images.append(src)
        if len(images) >= limit:
            break

    return images