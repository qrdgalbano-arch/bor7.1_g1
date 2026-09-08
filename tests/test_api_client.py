"""Tests for API client request and response handling."""

from unittest.mock import Mock, patch

import requests

from src.api_client import get_ip_information


def test_api_returns_incomplete_data():
    """Confirm partial API data is returned for safe display."""
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"ip": "8.8.8.8"}

    with patch("src.api_client.requests.get", return_value=fake_response):
        data = get_ip_information("8.8.8.8")

    assert data == {"ip": "8.8.8.8"}


def test_api_request_failure(capsys):
    """Confirm connection failures return None and display a simple message."""
    with patch(
        "src.api_client.requests.get",
        side_effect=requests.exceptions.ConnectionError(),
    ):
        data = get_ip_information("8.8.8.8")

    captured = capsys.readouterr()

    assert data is None
    assert "No internet connection" in captured.out


def test_api_timeout(capsys):
    """Confirm timeouts return None and display a simple message."""
    with patch(
        "src.api_client.requests.get",
        side_effect=requests.exceptions.Timeout(),
    ):
        data = get_ip_information("8.8.8.8")

    captured = capsys.readouterr()

    assert data is None
    assert "The request took too long" in captured.out


def test_api_error_response(capsys):
    """Confirm API error JSON returns None and displays the API reason."""
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "error": True,
        "reason": "The IP address is invalid.",
    }

    with patch("src.api_client.requests.get", return_value=fake_response):
        data = get_ip_information("bad-ip")

    captured = capsys.readouterr()

    assert data is None
    assert "The IP address is invalid." in captured.out
