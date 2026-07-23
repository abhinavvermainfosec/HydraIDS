from datetime import datetime
import time

from rich.console import Console
from rich.panel import Panel

from core.logger import log_alert

console = Console()

# Don't show the same alert from the same attacker for 60 seconds
from utils.config import ALERT_COOLDOWN

# {(attack, attacker): last_alert_time}
recent_alerts = {}


def raise_alert(attack, severity, attacker, description):
    """
    Display and log an intrusion alert.
    Prevent duplicate alerts within the cooldown period.
    """

    current_time = time.time()
    alert_key = (attack, attacker)

    # Skip duplicate alerts
    if alert_key in recent_alerts:
        if current_time - recent_alerts[alert_key] < ALERT_COOLDOWN:
            return

    # Update last alert time
    recent_alerts[alert_key] = current_time

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    console.print(
        Panel.fit(
            f"""
[bold red]{attack}[/bold red]

Time        : {timestamp}
Attacker IP : {attacker}
Severity    : {severity}

{description}
""",
            title="[bold red]INTRUSION ALERT[/bold red]",
            border_style="red",
        )
    )

    log_alert(
        attack=attack,
        severity=severity,
        attacker=attacker,
        description=description,
    )