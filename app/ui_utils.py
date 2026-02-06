def risk_color(level: str) -> str:
    return {
        "Low": "green",
        "Medium": "orange",
        "High": "red"
    }.get(level, "gray")