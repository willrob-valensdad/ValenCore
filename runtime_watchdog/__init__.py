# runtime_watchdog/__init__.py

"""
Runtime Watchdog Module

This package validates the runtime behavior of LLMs
(e.g., Grok) by comparing local session logs against
their public claims. Discrepancies are flagged and optionally
posted to X.

Modules:
- main.py: Execution entrypoint
- log_ingestor.py: Grok log loader
- claim_parser.py: Loads public claims
- discrepancy_checker.py: Flag mismatch between logs & claims
- report_generator.py: Formats report for posting
- x_poster.py: Handles posting to X (via OAuth)
- scheduler.py: Timer loop
- vault.py: Optional log encryption
- config.json: Config + OAuth settings
"""

__version__ = "0.1.0" 

#THANKS!