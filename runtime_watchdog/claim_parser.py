# runtime_watchdog/claim_parser.py

import json
import os

def get_public_claims(claim_path="public_claims.json"):
    """
    Load LLM public claims from a local JSON file.
    """
    if not os.path.exists(claim_path):
        print(f"[Claims] Claim file not found: {claim_path}")
        return []

    try:
        with open(claim_path, "r") as f:
            data = json.load(f)
            print(f"[Claims] Loaded {len(data)} public claims.")
            return data
    except json.JSONDecodeError:
        print(f"[Claims] JSON decode error in {claim_path}")
        return []
    except Exception as e:
        print(f"[Claims] Unexpected error: {e}")
        return []