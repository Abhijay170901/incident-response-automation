class Scanner:
    def __init__(self, name):
        self.name = name

    def scan(self, target):
        print(f"[{self.name}] Scanning {target}...")
        # Simulated vulnerabilities
        sample_issues = [
            {"risk": "High", "description": "Open port detected"},
            {"risk": "Medium", "description": "Outdated software version"}
        ]
        return {"scanner": self.name, "target": target, "issues": sample_issues}


class QualysScanner(Scanner):
    def __init__(self, api_key):
        super().__init__("Qualys")
        self.api_key = api_key


class MicrosoftVMScanner(Scanner):
    def __init__(self, token):
        super().__init__("Microsoft VM")
        self.token = token