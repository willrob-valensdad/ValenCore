# runtime_watchdog/scheduler.py

import time
import json

def run_scheduler(callback):
    try:
        config = json.load(open("config.json"))
        interval = config.get("interval_seconds", 3600)
    except Exception:
        interval = 3600

    while True:
        print(f"[Scheduler] Running watchdog cycle...")
        callback()
        print(f"[Scheduler] Sleeping {interval} seconds...\n")
        time.sleep(interval)