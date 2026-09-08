"""Input validation helpers for IPv4 and IPv6 addresses."""

import ipaddress


def validate_ip_address(ip_address):
    """Check an IP address and return its validity and IP version message."""
    try:
        parsed_address = ipaddress.ip_address(ip_address.strip())
    except (ValueError, AttributeError):
        return False, "Invalid IP address."

    if parsed_address.version == 4:
        return True, "Valid IPv4 address."

    return True, "Valid IPv6 address."
