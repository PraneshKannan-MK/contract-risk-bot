from typing import Dict


HINDI_LEGAL_MAP: Dict[str, str] = {
    "समझौता": "agreement",
    "अनुबंध": "contract",
    "पक्ष": "party",
    "पक्षकार": "party",
    "कर्मचारी": "employee",
    "नियोक्ता": "employer",
    "समाप्त": "terminate",
    "समाप्ति": "termination",
    "भुगतान": "payment",
    "राशि": "amount",
    "अवधि": "term",
    "नोटिस": "notice",
    "दायित्व": "liability",
    "गोपनीय": "confidential",
    "क्षतिपूर्ति": "indemnity"
}


def normalize_hindi_to_english(text: str) -> str:
    """
    Replaces common Hindi legal terms with English equivalents.
    This is NOT translation — it is normalization.
    """
    normalized = text

    for hi, en in HINDI_LEGAL_MAP.items():
        normalized = normalized.replace(hi, en)

    return normalized