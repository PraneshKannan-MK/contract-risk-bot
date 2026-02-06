from core.risk_engine import calculate_clause_risk


def test_high_risk_clause():
    analysis = {
        "ambiguous": True,
        "potential_issues": ["unilateral_termination"],
        "nature": "prohibition"
    }
    result = calculate_clause_risk(analysis)
    assert result["risk_level"] in ["Medium", "High"]