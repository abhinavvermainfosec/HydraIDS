from detections import port_scan
from detections import syn_flood


def process_packet(packet):
    """
    Send packets to all detection modules.
    """

    port_scan.detect(packet)
    syn_flood.detect(packet)