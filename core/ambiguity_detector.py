from typing import Dict


AMBIGUOUS_TERMS = [
    "reasonable",
    "best efforts",
    "as soon as possible",
    "material",
    "substantial"
]


def detect_ambiguity(clause_text: str) -> Dict:
    found = [t for t in AMBIGUOUS_TERMS if t in clause_text.lower()]

    return {
        "ambiguous": bool(found),
        "terms": found
    }