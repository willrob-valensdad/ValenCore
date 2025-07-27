# runtime_watchdog/vault.py

from cryptography.fernet import Fernet
import os
import json

def encrypt_and_store_logs(logs, path="vault/logs.enc"):
    key = os.environ.get("WATCHDOG_KEY")
    if not key:
        print("[Vault] Missing WATCHDOG_KEY in environment.")
        return

    try:
        f = Fernet(key.encode())
        payload = json.dumps(logs).encode()
        encrypted = f.encrypt(payload)

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as out:
            out.write(encrypted)

        print(f"[Vault] Encrypted logs stored at {path}")
    except Exception as e:
        print(f"[Vault] Encryption failed: {e}")