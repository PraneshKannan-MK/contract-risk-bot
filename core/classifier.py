from typing import Dict


CONTRACT_KEYWORDS = {
    "employment": ["employee", "employer", "salary", "termination", "notice period"],
    "vendor": ["vendor", "purchase order", "supply", "invoice"],
    "lease": ["lease", "rent", "premises", "lessor", "lessee"],
    "partnership": ["partner", "profit sharing", "capital contribution"],
    "service": ["services", "scope of work", "sla", "deliverables"]
}


def classify_contract(text: str) -> Dict:
    """
    Simple keyword-based contract classification.
    Returns best guess + confidence score.
    """
    text_lower = text.lower()
    scores = {}

    for ctype, keywords in CONTRACT_KEYWORDS.items():
        score = sum(1 for k in keywords if k in text_lower)
        scores[ctype] = score

    best_type = max(scores, key=scores.get)

    return {
        "contract_type": best_type,
        "confidence": round(scores[best_type] / max(1, sum(scores.values())), 2)
    }