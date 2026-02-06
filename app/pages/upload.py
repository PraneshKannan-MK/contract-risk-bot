import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from preprocessing.pdf_parser import extract_text_from_pdf
from preprocessing.docx_parser import extract_text_from_docx
from preprocessing.text_cleaner import clean_text
from multilingual.language_detector import detect_language
from multilingual.hindi_normalizer import normalize_hindi_to_english

st.header("📤 Upload Contract")

uploaded_file = st.file_uploader(
    "Upload a contract (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.success("File uploaded successfully")

    if uploaded_file.name.endswith(".pdf"):
        data = extract_text_from_pdf(uploaded_file)
        raw_text = data["full_text"]
    else:
        data = extract_text_from_docx(uploaded_file)
        raw_text = data["full_text"]

    language = detect_language(raw_text)

    if language == "hi":
        processed_text = normalize_hindi_to_english(raw_text)
        st.info("Hindi contract detected – normalized for analysis")
    else:
        processed_text = raw_text

    cleaned_text = clean_text(processed_text)

    st.session_state["contract_text"] = cleaned_text
    st.session_state["language"] = language

    st.text_area(
        "Extracted Contract Text (preview)",
        cleaned_text[:3000],
        height=300
    )