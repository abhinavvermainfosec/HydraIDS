from scapy.all import sniff

from core.parser import parse_packet, display_packet


def packet_callback(packet):
    parsed_packet = parse_packet(packet)

    if parsed_packet is None:
        return

    display_packet(parsed_packet)


def start_capture(interface):
    print(f"\n[*] Listening on {interface}...")
    print("[*] Press Ctrl+C to stop.\n")

    sniff(
        iface=interface,
        prn=packet_callback,
        store=False
    )