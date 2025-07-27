# runtime_watchdog/x_poster.py

from oauth import get_client
import json

def post_to_x(text):
    config = json.load(open("config.json"))
    debug = config.get("posting", {}).get("debug_mode", True)
    enabled = config.get("posting", {}).get("enabled", True)

    if not enabled:
        print("[Poster] Posting disabled in config.")
        return

    if debug:
        print("[Poster] DEBUG MODE — would post:\n", text)
    else:
        client = get_client()
        if client:
            client.create_tweet(text=text)
        else:
            print("[Poster] OAuth client not configured.")