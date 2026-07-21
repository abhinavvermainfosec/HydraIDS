from detections import port_scan


def process_packet(packet):
    """
    Send the parsed packet to all detection modules.
    """

    # Port Scan Detection
    port_scan.detect(packet)