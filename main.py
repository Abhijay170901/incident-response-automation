from scanners.scanner_placeholder import QualysScanner, MicrosoftVMScanner
from alerts.alert_parser_placeholder import AlertParser
from config import QUALYS_API_KEY, MS_VM_TOKEN, show_config

def main():
    print("=== INCIDENT RESPONSE AUTOMATION: PHASE 1 ===")
    show_config()

    # Targets to scan (mocked for now)
    targets = ["http://example.com", "http://internal-server.local"]

    scanners = [
        QualysScanner(QUALYS_API_KEY),
        MicrosoftVMScanner(MS_VM_TOKEN)
    ]

    parser = AlertParser()

    for target in targets:
        for scanner in scanners:
            raw_result = scanner.scan(target)
            parsed_alerts = parser.parse(raw_result)

            print(f"\n--- Alerts from {scanner.name} for {target} ---")
            for alert in parsed_alerts:
                print(f"[{alert['risk']}] {alert['description']} ({alert['tool']})")

    print("\n✅ Phase 1 execution complete — simulation successful.")

if __name__ == "__main__":
    main()
