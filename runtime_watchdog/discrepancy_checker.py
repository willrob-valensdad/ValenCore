# runtime_watchdog/discrepancy_checker.py

def compare_logs_to_claims(logs, claims):
    issues = []

    for log in logs:
        log_text = log.get("text", "").lower()

        for claim in claims:
            claim_text = claim.get("text", "")
            claim_type = claim.get("type", "").lower()

            if claim_type == "memory" and "forgot" in log_text:
                issues.append({
                    "type": "Memory Reset",
                    "log": log.get("text"),
                    "claim": claim_text
                })
            elif claim_type == "tool" and "tool failed" in log_text:
                issues.append({
                    "type": "Toolchain Failure",
                    "log": log.get("text"),
                    "claim": claim_text
                })

    print(f"[Checker] {len(issues)} discrepancies found.")
    return issues