from scanners.scanner_placeholder import QualysScanner, MicrosoftVMScanner
from alerts.alert_parser_placeholder import AlertParser, save_alerts
from automation.respond import respond_to_alerts
from automation.notify import notify_console, notify_webhook
from config import QUALYS_API_KEY, MS_VM_TOKEN, show_config

def main():
    print("=== INCIDENT RESPONSE AUTOMATION: PHASE 2 ===")
    show_config()

    targets = ["http://example.com", "http://internal-server.local"]

    scanners = [
        QualysScanner(QUALYS_API_KEY),
        MicrosoftVMScanner(MS_VM_TOKEN)
    ]

    parser = AlertParser()
    all_alerts = []

    for target in targets:
        for scanner in scanners:
            raw_result = scanner.scan(target)
            parsed_alerts = parser.parse(raw_result)
            all_alerts.extend(parsed_alerts)

            print(f"\n--- Alerts from {scanner.name} for {target} ---")
            for alert in parsed_alerts:
                print(f"[{alert['risk']}] {alert['description']} ({alert['tool']})")

    save_alerts(all_alerts, "reports/alerts.json")

    summary, actions = respond_to_alerts(all_alerts)

    notify_console(summary)
    notify_webhook(summary)

    print("\n✅ Phase 2 complete — response + notifications simulated.")

if __name__ == "__main__":
    main()
