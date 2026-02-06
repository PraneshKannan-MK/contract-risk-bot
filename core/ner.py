import re
from typing import Dict, List


DATE_PATTERN = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
AMOUNT_PATTERN = r'(₹|\$|Rs\.?)\s?\d+(?:,\d+)*(?:\.\d+)?'
JURISDICTION_PATTERN = r'\b(India|Tamil Nadu|Karnataka|Delhi|Mumbai)\b'


def extract_entities(text: str) -> Dict[str, List[str]]:
    """
    Extract key legal entities using regex heuristics.
    """
    return {
        "dates": re.findall(DATE_PATTERN, text),
        "amounts": re.findall(AMOUNT_PATTERN, text),
        "jurisdictions": re.findall(JURISDICTION_PATTERN, text),
    }