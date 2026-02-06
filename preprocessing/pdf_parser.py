from typing import Dict
import pdfplumber


def extract_text_from_pdf(file_path: str) -> Dict:
    """
    Extract raw text from a text-based PDF.
    Returns dict with pages + full_text for traceability.
    """
    pages = []
    full_text = []

    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages.append({
                    "page_number": i + 1,
                    "text": text.strip()
                })
                full_text.append(text.strip())

    return {
        "pages": pages,
        "full_text": "\n".join(full_text)
    }