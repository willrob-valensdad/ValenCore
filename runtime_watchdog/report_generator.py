# runtime_watchdog/report_generator.py

def generate_report(discrepancies):
    header = "[Runtime Watchdog] Discrepancies Detected:\n"
    body = ""

    for d in discrepancies:
        body += f"\n🔻 Type: {d['type']}\nGrok Log: {d['log']}\nClaim: {d['claim']}\n"

    footer = "\n#RuntimeWatchdog #LLMTransparency"
    return header + body + footer