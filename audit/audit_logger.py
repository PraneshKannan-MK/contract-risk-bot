import json
import uuid
from datetime import datetime
from typing import Dict


AUDIT_LOG_FILE = "audit/audit_log.json"


def log_event(event_type: str, details: Dict):
    """
    Logs audit events for traceability.
    Stores metadata only — no raw contract text.
    """
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "details": details
    }

    try:
        with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(event)

    with open(AUDIT_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)