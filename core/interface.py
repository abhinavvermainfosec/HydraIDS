from scapy.all import get_if_list


def get_interfaces():
    """Return all available network interfaces."""
    return get_if_list()


def display_interfaces():
    interfaces = get_interfaces()

    print("\nAvailable Interfaces\n")

    for index, interface in enumerate(interfaces, start=1):
        print(f"[{index}] {interface}")

    return interfaces