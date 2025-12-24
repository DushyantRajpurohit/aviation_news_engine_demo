import yaml
from pathlib import Path

from ingestion.discover import discover_latest_article
from ingestion.rss_detector import auto_detect_rss
from ingestion.sitemap_reader import get_latest_from_sitemap
from processing.extract import extract_article
from processing.classify import classify_article
from media.image_extract import extract_images
from media.image_save import save_image
from storage.db import save_article

BASE_DIR = Path(__file__).resolve().parent
sources = yaml.safe_load((BASE_DIR / "config" / "sources.yaml").open())["sources"]

for source in sources:
    print(f"\n🆕 Processing {source['name']}")

    rss_url = source.get("rss")
    website = source.get("website")

    if not rss_url and website:
        rss_url = auto_detect_rss(website)

    if rss_url:
        url = discover_latest_article(rss_url)
    elif website:
        url = get_latest_from_sitemap(website)
    else:
        url = None

    if not url:
        print("⚠️ No article found, skipping")
        continue

    try:
        headline, text = extract_article(url)
        if not text:
            print("⚠️ No content extracted")
            continue

        category = classify_article(text)
        if category == "General":
            category = source.get("category_focus", "General")

        images = extract_images(url)
        image_path = None
        if images:
            image_path = save_image(images[0], category, url)

        save_article(
            url=url,
            source=source["name"],
            headline=headline,
            category=category,
            content=text,
            image_path=image_path
        )

        print(f"✔ Saved latest article → {category}")

    except Exception as e:
        print(f"❌ Failed: {e}")