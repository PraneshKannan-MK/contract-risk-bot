from typing import Dict


NON_COMPLIANT_PATTERNS = {
    "unilateral_termination": ["terminate at any time without notice"],
    "excessive_penalty": ["penalty of", "liquidated damages exceeding"],
    "non_compete": ["non compete", "restraint of trade"]
}


def check_compliance(clause_text: str) -> Dict:
    issues = []

    text = clause_text.lower()
    for issue, patterns in NON_COMPLIANT_PATTERNS.items():
        if any(p in text for p in patterns):
            issues.append(issue)

    return {
        "potential_issues": issues,
        "compliant": len(issues) == 0
    }