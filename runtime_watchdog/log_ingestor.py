# runtime_watchdog/log_ingestor.py

import json
import os

def get_grok_logs(log_path="grok_logs.json"):
    """
    Load Grok session logs from a local JSON file.
    Returns an array of log entries or an empty list if missing.
    """

    if not os.path.exists(log_path):
        print(f"[Ingestor] Log file not found: {log_path}")
        return []

    try:
        with open(log_path, "r") as f:
            data = json.load(f)
            print(f"[Ingestor] Loaded {len(data)} log entries from {log_path}")
            return data
    except json.JSONDecodeError:
        print(f"[Ingestor] Error decoding JSON in {log_path}")
        return []
    except Exception as e:
        print(f"[Ingestor] Unexpected error loading logs: {e}")
        return []