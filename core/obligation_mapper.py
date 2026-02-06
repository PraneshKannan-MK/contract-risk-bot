from typing import Dict


OBLIGATION_TERMS = ["shall", "must", "is required to"]
RIGHT_TERMS = ["may", "is entitled to", "can"]
PROHIBITION_TERMS = ["shall not", "must not", "is prohibited from"]


def classify_clause_nature(clause_text: str) -> Dict:
    text = clause_text.lower()

    if any(t in text for t in PROHIBITION_TERMS):
        nature = "prohibition"
    elif any(t in text for t in OBLIGATION_TERMS):
        nature = "obligation"
    elif any(t in text for t in RIGHT_TERMS):
        nature = "right"
    else:
        nature = "neutral"

    return {
        "nature": nature
    }