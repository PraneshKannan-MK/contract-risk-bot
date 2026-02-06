import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from core.classifier import classify_contract
from core.ner import extract_entities
from reports.report_generator import generate_contract_report
from reports.pdf_exporter import export_report_to_pdf

st.header("📊 Risk Summary Report")


if "clause_results" not in st.session_state:
    st.warning("Run analysis first.")
    st.stop()

contract_text = st.session_state["contract_text"]

contract_type = classify_contract(contract_text)
entities = extract_entities(contract_text)

report = generate_contract_report(
    contract_type=contract_type,
    entities=entities,
    clause_results=st.session_state["clause_results"]
)

st.subheader("Overall Risk")
st.metric("Risk Level", report["contract_metadata"]["overall_risk_level"])
st.metric("Risk Score", report["contract_metadata"]["overall_risk_score"])

st.subheader("Summary")
st.write(report["summary"])

st.subheader("Recommendations")
for rec in report["recommendations"]:
    st.write("- ", rec)

if st.button("📄 Export PDF"):
    export_report_to_pdf(report, "contract_risk_report.pdf")
    st.success("PDF exported as contract_risk_report.pdf")