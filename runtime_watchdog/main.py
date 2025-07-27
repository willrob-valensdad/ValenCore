# runtime_watchdog/main.py

from scheduler import run_scheduler
from log_ingestor import get_grok_logs
from claim_parser import get_public_claims
from discrepancy_checker import compare_logs_to_claims
from report_generator import generate_report
from x_poster import post_to_x
from vault import encrypt_and_store_logs

def watchdog_cycle():
    logs = get_grok_logs()
    claims = get_public_claims()
    discrepancies = compare_logs_to_claims(logs, claims)

    if discrepancies:
        report = generate_report(discrepancies)
        post_to_x(report)
        encrypt_and_store_logs(logs)
    else:
        print("[Watchdog] No discrepancies found in this cycle.")

if __name__ == "__main__":
    print("[Watchdog] Starting runtime watchdog scheduler...")
    run_scheduler(watchdog_cycle)