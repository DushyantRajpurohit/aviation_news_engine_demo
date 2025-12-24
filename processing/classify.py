def classify_article(text):
    t = text.lower()

    if "cargo" in t:
        return "Cargo"
    if "maintenance" in t or "overhaul" in t:
        return "MRO"
    if "military" in t or "defence" in t:
        return "Defence"
    if "airline" in t:
        return "Commercial"
    if "revenue" in t or "profit" in t:
        return "Business"

    return "General"