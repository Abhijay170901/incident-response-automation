import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

QUALYS_API_KEY = os.getenv("QUALYS_API_KEY")
MS_VM_TOKEN = os.getenv("MS_VM_TOKEN")
TARGETS_FILE = os.getenv("TARGETS_FILE", "targets.txt")
REPORTS_DIR = os.getenv("REPORTS_DIR", "reports/")

def show_config():
    print("[+] Configuration loaded:")
    print(f"QUALYS_API_KEY: {QUALYS_API_KEY}")
    print(f"MS_VM_TOKEN: {MS_VM_TOKEN}")
    print(f"TARGETS_FILE: {TARGETS_FILE}")
    print(f"REPORTS_DIR: {REPORTS_DIR}")