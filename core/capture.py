from scapy.all import sniff

import utils.config as config
from core.detector import process_packet
from core.parser import display_packet, parse_packet


def packet_callback(packet):
    parsed_packet = parse_packet(packet)

    if parsed_packet is None:
        return

    if config.DEBUG:
        display_packet(parsed_packet)

    process_packet(parsed_packet)


def start_capture(interface):
    print(f"\n[*] Listening on {interface}...")
    print("[*] Press Ctrl+C to stop.\n")

    sniff(
        iface=interface,
        prn=packet_callback,
        store=False
    )