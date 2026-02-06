import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "settings.yaml"

with open(CONFIG_PATH, "r") as f:
    SETTINGS = yaml.safe_load(f)

RISK_THRESHOLDS = SETTINGS["risk_thresholds"]
LANGUAGE = SETTINGS["language"]
FEATURES = SETTINGS["features"]
AUDIT = SETTINGS["audit"]