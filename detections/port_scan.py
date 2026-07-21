import time

from core.alerts import raise_alert

# Detection configuration
TIME_WINDOW = 30          # seconds
PORT_THRESHOLD = 5        # unique ports

# {source_ip: {destination_port: timestamp}}
scan_tracker = {}


def detect(packet):
    """
    Detect TCP SYN Port Scans.
    """

    # Only inspect TCP packets
    if packet["protocol"] != "TCP":
        return

    # Only count SYN packets
    if "S" not in packet["flags"]:
        return

    src_ip = packet["src_ip"]
    dst_port = packet["dst_port"]

    current_time = time.time()

    # Create tracker for new source
    if src_ip not in scan_tracker:
        scan_tracker[src_ip] = {}

    # Record destination port
    scan_tracker[src_ip][dst_port] = current_time

    # Remove expired ports
    scan_tracker[src_ip] = {
        port: timestamp
        for port, timestamp in scan_tracker[src_ip].items()
        if current_time - timestamp <= TIME_WINDOW
    }

    unique_ports = len(scan_tracker[src_ip])

    # Trigger alert
    if unique_ports >= PORT_THRESHOLD:
        raise_alert(
            attack="TCP SYN Port Scan",
            severity="HIGH",
            attacker=src_ip,
            description=f"{unique_ports} unique ports detected within {TIME_WINDOW} seconds."
        )

        # Prevent repeated alerts for the same scan
        scan_tracker[src_ip].clear()