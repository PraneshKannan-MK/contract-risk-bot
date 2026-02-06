import re
from typing import List, Dict


CLAUSE_PATTERNS = [
    r'\b\d+\.\s',        # 1. 2. 3.
    r'\b\d+\.\d+\s',     # 1.1 1.2
    r'\b[A-Z][a-z]+:',   # Definitions:
]


def segment_clauses(text: str) -> List[Dict]:
    """
    Splits contract text into clauses using heuristic rules.
    """
    clauses = []
    raw_chunks = re.split(r'(?=\n?\d+\.)', text)

    for idx, chunk in enumerate(raw_chunks):
        cleaned = chunk.strip()
        if len(cleaned) < 30:
            continue

        clauses.append({
            "clause_id": f"C{idx+1}",
            "text": cleaned
        })

    return clauses