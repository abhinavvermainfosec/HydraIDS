from scapy.layers.inet import IP, TCP, UDP, ICMP
from rich.console import Console
from rich.panel import Panel

console = Console()


def parse_packet(packet):
    """
    Parse a Scapy packet into a normalized dictionary.
    Returns None if the packet is not IPv4.
    """

    if not packet.haslayer(IP):
        return None

    parsed = {
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "protocol": "UNKNOWN",
        "src_port": "-",
        "dst_port": "-",
        "flags": "-",
        "length": len(packet)
    }

    if packet.haslayer(TCP):
        parsed["protocol"] = "TCP"
        parsed["src_port"] = packet[TCP].sport
        parsed["dst_port"] = packet[TCP].dport
        parsed["flags"] = str(packet[TCP].flags)

    elif packet.haslayer(UDP):
        parsed["protocol"] = "UDP"
        parsed["src_port"] = packet[UDP].sport
        parsed["dst_port"] = packet[UDP].dport

    elif packet.haslayer(ICMP):
        parsed["protocol"] = "ICMP"

    return parsed


def display_packet(packet):
    """
    Pretty-print a parsed packet.
    """

    console.print(
        Panel.fit(
            f"""[bold cyan]Protocol[/bold cyan] : {packet['protocol']}
[bold green]Source[/bold green]   : {packet['src_ip']}:{packet['src_port']}
[bold yellow]Target[/bold yellow]   : {packet['dst_ip']}:{packet['dst_port']}
[bold magenta]Flags[/bold magenta]    : {packet['flags']}
[bold white]Length[/bold white]   : {packet['length']} bytes""",
            title="[bold blue]Captured Packet[/bold blue]",
            border_style="cyan",
        )
    )