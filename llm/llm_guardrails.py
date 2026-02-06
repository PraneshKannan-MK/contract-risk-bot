from llm.llm_client import call_llama
from llm.llm_guardrails import build_safe_prompt

with open("llm/prompts/contract_summary.txt") as f:
    template = f.read()

prompt = build_safe_prompt(
    template,
    clause_text=""  # replaced with formatted inputs
)

summary = call_llama(prompt)