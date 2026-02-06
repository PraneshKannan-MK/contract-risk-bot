from typing import List, Dict
import re

from preprocessing.clause_segmenter import segment_clauses


# High-level clause categories judges expect
CLAUSE_CATEGORIES = {
    "termination": ["terminate", "termination", "end this agreement"],
    "payment": ["payment", "fee", "invoice", "consideration"],
    "confidentiality": ["confidential", "non-disclosure"],
    "indemnity": ["indemnify", "hold harmless"],
    "liability": ["liability", "liable", "damages"],
    "governing_law": ["governing law", "jurisdiction", "courts"],
    "intellectual_property": ["intellectual property", "ip", "ownership"],
    "non_compete": ["non compete", "restraint of trade"],
    "auto_renewal": ["auto renew", "automatically renew"],
}


def extract_clause_title(text: str) -> str:
    """
    Attempts to extract a clause title if present.
    Example: 'Termination: Either party may...'
    """
    match = re.match(r"^([A-Z][A-Za-z\s]{3,40}):", text)
    if match:
        return match.group(1).strip()
    return ""


def classify_clause_category(text: str) -> str:
    """
    Assigns a high-level category based on keyword presence.
    """
    text_lower = text.lower()

    for category, keywords in CLAUSE_CATEGORIES.items():
        if any(k in text_lower for k in keywords):
            return category

    return "general"


def extract_clauses(contract_text: str) -> List[Dict]:
    """
    Full clause extraction pipeline:
    - segmentation (preprocessing)
    - title detection
    - category classification
    """
    raw_clauses = segment_clauses(contract_text)
    extracted = []

    for idx, clause in enumerate(raw_clauses, start=1):
        text = clause["text"]

        extracted.append({
            "clause_id": f"CL-{idx:03d}",
            "title": extract_clause_title(text),
            "category": classify_clause_category(text),
            "text": text
        })

    return extracted