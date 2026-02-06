from typing import Dict
from docx import Document


def extract_text_from_docx(file_path: str) -> Dict:
    """
    Extract text from DOC/DOCX files.
    """
    doc = Document(file_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

    return {
        "paragraphs": paragraphs,
        "full_text": "\n".join(paragraphs)
    }