import os
import requests
import uuid

BASE_DIR = "images"

def save_image(image_url, category, article_url):
    # Ensure category directory exists
    category_dir = os.path.join(BASE_DIR, category)
    os.makedirs(category_dir, exist_ok=True)

    # Generate a guaranteed-safe filename
    filename = f"image-{uuid.uuid4().hex[:12]}"

    # Extract extension safely
    ext = image_url.split("?")[0].split(".")[-1]
    if not ext.isalpha() or len(ext) > 5:
        ext = "jpg"

    relative_path = f"{category}/{filename}.{ext}"
    full_path = os.path.join(BASE_DIR, relative_path)

    r = requests.get(image_url, timeout=10, verify=False)
    r.raise_for_status()

    with open(full_path, "wb") as f:
        f.write(r.content)

    return relative_path