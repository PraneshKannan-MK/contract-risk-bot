from typing import List, Dict


def generate_contract_report(
    contract_type: Dict,
    entities: Dict,
    clause_results: List[Dict]
) -> Dict:
    """
    Generates a structured contract risk report.
    """

    total_score = sum(c["risk_score"] for c in clause_results)
    avg_score = round(total_score / max(1, len(clause_results)), 2)

    if avg_score <= 2:
        overall_level = "Low"
    elif avg_score <= 5:
        overall_level = "Medium"
    else:
        overall_level = "High"

    high_risk = [c for c in clause_results if c["risk_level"] == "High"]

    return {
        "contract_metadata": {
            "contract_type": contract_type["contract_type"],
            "overall_risk_level": overall_level,
            "overall_risk_score": avg_score
        },
        "parties": entities.get("parties", []),
        "key_dates": entities.get("dates", []),
        "financials": entities.get("amounts", []),
        "clause_analysis": clause_results,
        "high_risk_clauses": high_risk,
        "summary": generate_summary(overall_level, high_risk),
        "recommendations": generate_recommendations(high_risk)
    }


def generate_summary(overall_level: str, high_risk_clauses: List[Dict]) -> str:
    if overall_level == "Low":
        return "The contract presents low overall risk with standard commercial terms."
    if overall_level == "Medium":
        return "The contract contains moderate risk clauses that should be reviewed carefully."
    return f"The contract contains {len(high_risk_clauses)} high-risk clauses that may require renegotiation."


def generate_recommendations(high_risk_clauses: List[Dict]) -> List[str]:
    recommendations = []

    for clause in high_risk_clauses:
        recommendations.append(
            f"Review clause {clause['clause_id']} due to {', '.join(clause.get('compliance_issues', [])) or 'elevated risk'}."
        )

    return recommendations