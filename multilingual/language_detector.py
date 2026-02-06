def detect_language(text: str) -> str:
    """
    Detects Hindi vs English based on Unicode range.
    Returns: 'hi' or 'en'
    """
    for ch in text:
        if '\u0900' <= ch <= '\u097F':  # Devanagari block
            return "hi"
    return "en"