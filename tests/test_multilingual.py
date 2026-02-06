from multilingual.language_detector import detect_language
from multilingual.hindi_normalizer import normalize_hindi_to_english


def test_hindi_detection_and_normalization():
    text = "यह एक अनुबंध है"
    assert detect_language(text) == "hi"
    normalized = normalize_hindi_to_english(text)
    assert "contract" in normalized.lower()