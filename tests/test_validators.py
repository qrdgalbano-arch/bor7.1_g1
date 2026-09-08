"""Tests for IPv4 and IPv6 validation."""

import pytest

from src.validators import validate_ip_address


@pytest.mark.parametrize(
    "ip_address, expected_message",
    [
        ("8.8.8.8", "Valid IPv4 address."),
        ("1.1.1.1", "Valid IPv4 address."),
    ],
)
def test_valid_ipv4_address(ip_address, expected_message):
    """Confirm valid IPv4 addresses are accepted."""
    is_valid, message = validate_ip_address(ip_address)

    assert is_valid is True
    assert message == expected_message


def test_valid_ipv6_address():
    """Confirm a valid IPv6 address is accepted."""
    is_valid, message = validate_ip_address("2001:4860:4860::8888")

    assert is_valid is True
    assert message == "Valid IPv6 address."


@pytest.mark.parametrize(
    "ip_address",
    [
        "999.999.999.999",
        "hello",
        "192.168.1",
        "",
    ],
)
def test_invalid_ip_address(ip_address):
    """Confirm invalid IP inputs are rejected."""
    is_valid, message = validate_ip_address(ip_address)

    assert is_valid is False
    assert message == "Invalid IP address."
