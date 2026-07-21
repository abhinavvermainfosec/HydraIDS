from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "alerts.log"


def log_alert(attack, severity, attacker, description):
    """
    Write an intrusion alert to the log file.
    """

    LOG_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as logfile:
        logfile.write(f"[{timestamp}]\n")
        logfile.write(f"Attack      : {attack}\n")
        logfile.write(f"Severity    : {severity}\n")
        logfile.write(f"Attacker IP : {attacker}\n")
        logfile.write(f"Description : {description}\n")
        logfile.write("-" * 50 + "\n\n")