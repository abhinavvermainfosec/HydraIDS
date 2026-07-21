from detections import port_scan


def process_packet(packet):
    """
    Pass every parsed packet to all detection modules.
    """

    port_scan.detect(packet)