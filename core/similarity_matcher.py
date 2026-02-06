from typing import Dict
from difflib import SequenceMatcher


def similarity_score(a: str, b: str) -> float:
    return round(SequenceMatcher(None, a.lower(), b.lower()).ratio(), 2)


def match_to_template(clause_text: str, template_clauses: Dict) -> Dict:
    best_match = None
    best_score = 0.0

    for tid, template_text in template_clauses.items():
        score = similarity_score(clause_text, template_text)
        if score > best_score:
            best_score = score
            best_match = tid

    return {
        "matched_template": best_match,
        "similarity": best_score
    }