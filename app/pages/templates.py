import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import json
import os
import streamlit as st

TEMPLATE_DIR = "templates"

st.header("📑 Standard Contract Templates")
st.caption("Reference-only SME-friendly contract clause templates")

template_files = [
    f for f in os.listdir(TEMPLATE_DIR)
    if f.endswith(".json")
]

if not template_files:
    st.warning("No templates found.")
    st.stop()

selected_template = st.selectbox(
    "Select a contract template",
    template_files
)

template_path = os.path.join(TEMPLATE_DIR, selected_template)

with open(template_path, "r", encoding="utf-8") as f:
    template_data = json.load(f)

st.subheader(template_data.get("name", selected_template))

clauses = template_data.get("clauses", {})

if not clauses:
    st.info("This template has no clauses yet.")
else:
    for title, text in clauses.items():
        with st.expander(title.replace("_", " ").title()):
            st.write(text)

st.download_button(
    label="⬇️ Download Template (JSON)",
    data=json.dumps(template_data, indent=2),
    file_name=selected_template,
    mime="application/json"
)

st.markdown("---")
st.caption(
    "⚠️ These templates are for reference purposes only and do not constitute legal advice."
)