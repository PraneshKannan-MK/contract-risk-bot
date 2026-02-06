# Contract Analysis & Risk Assessment Bot

GenAI-assisted legal risk analysis platform for Indian SMEs.

---

## 🔍 Overview

The **Contract Analysis & Risk Assessment Bot** helps small and medium businesses understand complex contract documents by automatically extracting clauses, identifying legal risks, and presenting insights in simple, business-friendly language.

The system focuses on explainability, deterministic risk scoring, and practical usability for non-legal users.

---

## ❓ Problem Statement

SMEs frequently enter into contracts without fully understanding:
- Unfavorable or unilateral clauses  
- Termination and liability risks  
- Compliance implications  

Manual legal review is costly and time-consuming. This project provides an automated, accessible alternative for early-stage contract risk assessment.

---

## ✅ Solution

The platform allows users to:
- Upload contract documents (PDF / DOCX)
- Perform clause-by-clause analysis
- Identify obligations, rights, and prohibitions
- Detect ambiguous and risky clauses
- Assign clause-level and overall risk scores
- Generate a clear risk summary report
- Refer to standard SME-friendly contract templates

---

## ✨ Key Features

- 📄 Contract upload (PDF, DOCX)
- 🧩 Clause & sub-clause extraction
- ⚖️ Obligation / Right / Prohibition detection
- 🚨 Risk identification (termination, indemnity, unilateral terms)
- 📊 Risk scoring (Low / Medium / High)
- 📝 Plain-language explanations
- 📁 PDF risk report export
- 📚 Standard contract templates
- 🔍 Deterministic, audit-friendly logic

---

## ⚙️ Risk Assessment Logic

- Clause risk is calculated using:
  - Ambiguity detection
  - Compliance issue flags
  - Nature of clause (obligation, right, prohibition)
- Weighted scoring is applied deterministically
- Configurable thresholds classify risk as:
  - **Low**
  - **Medium**
  - **High**

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Document Parsing:** pdfplumber, python-docx  
- **Configuration:** YAML  
- **GenAI (Optional):** Ollama (LLaMA 3.2 1B via HTTP API)  
- **Containerization:** Docker  

---

## 🚀 Live Deployment

**Live URL:**  
http://103.158.43.36:8502

**Network URL:**
http://10.24.6.170:8502


---

## ▶️ Running Locally

```bash
git clone https://github.com/PraneshKannan-MK/contract-risk-bot.git
cd contract-risk-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
