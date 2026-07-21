import argparse

import utils.config as config
from core.capture import start_capture
from core.interface import display_interfaces
from utils.banner import print_banner


def main():
    parser = argparse.ArgumentParser(
        description="HydraIDS - Python Intrusion Detection System"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Display every captured packet."
    )

    args = parser.parse_args()

    config.DEBUG = args.debug

    print_banner()

    interfaces = display_interfaces()

    while True:
        try:
            choice = int(input("\nSelect Interface > ")) - 1

            if 0 <= choice < len(interfaces):
                break

            print("[!] Invalid interface number.")

        except ValueError:
            print("[!] Please enter a valid number.")

    interface = interfaces[choice]

    print(f"\n[*] Selected Interface : {interface}")
    print(f"[*] Debug Mode         : {'ON' if config.DEBUG else 'OFF'}")

    start_capture(interface)


if __name__ == "__main__":
    main()