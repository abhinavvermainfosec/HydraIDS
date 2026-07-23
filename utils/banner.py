from rich.console import Console
from rich.panel import Panel

console = Console()


def print_banner():
    banner = r"""
 _   _           _             ___ ____  ____
| | | |_   _  __| |_ __ __ _  |_ _|  _ \/ ___|
| |_| | | | |/ _` | '__/ _` |  | || | | \___ \
|  _  | |_| | (_| | | | (_| |  | || |_| |___) |
|_| |_|\__, |\__,_|_|  \__,_| |___|____/|____/
        |___/
"""

    console.print(
        Panel.fit(
            f"[bold cyan]{banner}[/bold cyan]\n"
            "[green]HydraIDS v0.2.0[/green]\n"
            "Lightweight CLI Intrusion Detection System",
            border_style="cyan",
        )
    )