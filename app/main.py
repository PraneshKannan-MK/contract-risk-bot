import streamlit as st

st.set_page_config(
    page_title="Contract Risk Assessment Bot",
    layout="wide"
)

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("GenAI-assisted legal risk analysis for Indian SMEs")

st.markdown("""
Upload a contract to:
- Identify risky clauses
- Understand obligations & liabilities
- Get a plain-language risk summary
""")

st.sidebar.title("Navigation")
st.sidebar.markdown("""
Use the pages on the left to:
1. Upload a contract  
2. Analyze clauses  
3. Generate a risk report  
""")