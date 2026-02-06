from typing import Dict
from config.settings import RISK_THRESHOLDS

# Fixed, deterministic weights (do NOT overcomplicate this)
RISK_WEIGHTS = {
    "ambiguity": 2,
    "non_compliance": 3,
    "unilateral_terms": 3
}


def calculate_clause_risk(analysis: Dict) -> Dict:
    """
    Calculate risk score and level for a single clause.

    analysis expects keys like:
    - ambiguous: bool
    - potential_issues: list or None
    - nature: "obligation" | "right" | "prohibition"
    """

    score = 0

    # Ambiguous language increases risk
    if analysis.get("ambiguous"):
        score += RISK_WEIGHTS["ambiguity"]

    # Any compliance or legal issue flags
    if analysis.get("potential_issues"):
        score += RISK_WEIGHTS["non_compliance"]

    # Prohibitions / unilateral terms are higher risk
    if analysis.get("nature") == "prohibition":
        score += RISK_WEIGHTS["unilateral_terms"]

    # Risk level mapping (CONFIG-DRIVEN, NOT HARDCODED)
    if score <= RISK_THRESHOLDS["low"]:
        level = "Low"
    elif score <= RISK_THRESHOLDS["medium"]:
        level = "Medium"
    else:
        level = "High"

    return {
        "risk_score": score,
        "risk_level": level
    }