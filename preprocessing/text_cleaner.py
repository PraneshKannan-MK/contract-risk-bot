import re


def clean_text(text: str) -> str:
    """
    Basic legal text cleanup:
    - normalize spaces
    - remove repeated punctuation
    - keep legal structure intact
    """
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'_{2,}', '_', text)
    text = re.sub(r'-{2,}', '-', text)
    return text.strip()