import os
import json
import requests

def notify_console(summary):
    print("\n=== NOTIFY (Console) ===")
    print(json.dumps(summary, indent=2))

def notify_webhook(summary):
    url = os.getenv("SLACK_WEBHOOK_URL") or os.getenv("TEAMS_WEBHOOK_URL")
    if not url:
        print("[i] No WEBHOOK env var set; skipping webhook notify.")
        return

    text = f"IR Summary -> High:{summary.get('High',0)} | Medium:{summary.get('Medium',0)} | Low:{summary.get('Low',0)}"
    payload = {"text": text}

    try:
        r = requests.post(url, json=payload, timeout=10)
        print(f"[+] Webhook response: {r.status_code}")
    except Exception as e:
        print(f"[!] Webhook notify failed: {e}")
