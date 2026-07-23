import time

from core.alerts import raise_alert
from utils.config import (
    SYN_FLOOD_THRESHOLD,
    SYN_FLOOD_TIME_WINDOW,
)

# {source_ip: [timestamps]}
syn_tracker = {}


def detect(packet):
    """
    Detect TCP SYN Flood attacks.
    """

    if packet["protocol"] != "TCP":
        return

    if packet["flags"] != "S":
        return

    src_ip = packet["src_ip"]

    current_time = time.time()

    if src_ip not in syn_tracker:
        syn_tracker[src_ip] = []

    syn_tracker[src_ip].append(current_time)

    syn_tracker[src_ip] = [
        timestamp
        for timestamp in syn_tracker[src_ip]
        if current_time - timestamp <= SYN_FLOOD_TIME_WINDOW
    ]

    syn_count = len(syn_tracker[src_ip])

    if syn_count >= SYN_FLOOD_THRESHOLD:

        raise_alert(
            attack="TCP SYN Flood",
            severity="CRITICAL",
            attacker=src_ip,
            description=(
                f"{syn_count} SYN packets detected within "
                f"{SYN_FLOOD_TIME_WINDOW} seconds."
            ),
        )

        syn_tracker[src_ip].clear()