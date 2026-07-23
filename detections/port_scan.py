import time

from core.alerts import raise_alert
from utils.config import (
    PORT_SCAN_THRESHOLD,
    PORT_SCAN_TIME_WINDOW,
)

# {source_ip: {destination_port: timestamp}}
scan_tracker = {}


def detect(packet):
    """
    Detect TCP SYN Port Scans.
    """

    if packet["protocol"] != "TCP":
        return

    if packet["flags"] != "S":
        return

    src_ip = packet["src_ip"]
    dst_port = packet["dst_port"]

    current_time = time.time()

    if src_ip not in scan_tracker:
        scan_tracker[src_ip] = {}

    scan_tracker[src_ip][dst_port] = current_time

    scan_tracker[src_ip] = {
        port: timestamp
        for port, timestamp in scan_tracker[src_ip].items()
        if current_time - timestamp <= PORT_SCAN_TIME_WINDOW
    }

    unique_ports = len(scan_tracker[src_ip])

    if unique_ports >= PORT_SCAN_THRESHOLD:
        raise_alert(
            attack="TCP SYN Port Scan",
            severity="HIGH",
            attacker=src_ip,
            description=(
                f"{unique_ports} unique ports detected "
                f"within {PORT_SCAN_TIME_WINDOW} seconds."
            ),
        )

        scan_tracker[src_ip].clear()