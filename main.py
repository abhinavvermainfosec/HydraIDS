from utils.banner import print_banner
from core.interface import display_interfaces
from core.capture import start_capture


def main():
    print_banner()

    interfaces = display_interfaces()

    while True:
        try:
            choice = int(input("\nSelect Interface > "))

            if 1 <= choice <= len(interfaces):
                selected = interfaces[choice - 1]
                break

            print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")

    print(f"\n[*] Selected: {selected}")

    start_capture(selected)


if __name__ == "__main__":
    main()