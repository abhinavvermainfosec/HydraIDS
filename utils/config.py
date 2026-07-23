"""
HydraIDS Configuration

All configurable values should be defined here.
"""

# --------------------------------------------------
# General
# --------------------------------------------------

DEBUG = False


# --------------------------------------------------
# Port Scan Detection
# --------------------------------------------------

PORT_SCAN_TIME_WINDOW = 30      # seconds
PORT_SCAN_THRESHOLD = 5         # unique destination ports


# --------------------------------------------------
# SYN Flood Detection
# --------------------------------------------------

SYN_FLOOD_TIME_WINDOW = 2       # seconds
SYN_FLOOD_THRESHOLD = 100       # SYN packets


# --------------------------------------------------
# UDP Scan Detection
# --------------------------------------------------

UDP_SCAN_TIME_WINDOW = 30
UDP_SCAN_THRESHOLD = 5


# --------------------------------------------------
# ICMP Flood Detection
# --------------------------------------------------

ICMP_FLOOD_TIME_WINDOW = 2
ICMP_FLOOD_THRESHOLD = 100


# --------------------------------------------------
# Alert Manager
# --------------------------------------------------

ALERT_COOLDOWN = 60