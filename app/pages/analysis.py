import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from preprocessing.clause_segmenter import segment_clauses
from core.ambiguity_detector import detect_ambiguity
from core.obligation_mapper import classify_clause_nature
from core.compliance_checker import check_compliance
from core.risk_engine import calculate_clause_risk


st.header("🔍 Clause-by-Clause Analysis")

if "contract_text" not in st.session_state:
    st.warning("Please upload a contract first.")
    st.stop()

clauses = segment_clauses(st.session_state["contract_text"])
results = []

for clause in clauses:
    analysis = {"clause_id": clause["clause_id"], "text": clause["text"]}

    analysis.update(classify_clause_nature(clause["text"]))
    analysis.update(detect_ambiguity(clause["text"]))
    analysis.update(check_compliance(clause["text"]))
    analysis.update(calculate_clause_risk(analysis))

    results.append(analysis)

st.session_state["clause_results"] = results

for r in results:
    with st.expander(f"{r['clause_id']} | Risk: {r['risk_level']}"):
        st.write(r["text"])
        st.write("**Nature:**", r["nature"])
        st.write("**Ambiguous:**", r["ambiguous"])
        st.write("**Compliance Issues:**", r.get("potential_issues", []))