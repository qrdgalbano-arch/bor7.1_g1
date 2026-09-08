"""Tests for safe IP-information display formatting."""

from rich.console import Console

from src import formatter


def test_formatter_uses_not_available_for_missing_fields():
    """Confirm missing API fields display as Not available."""
    recording_console = Console(record=True, force_terminal=False, width=120)
    original_console = formatter.console
    formatter.console = recording_console

    try:
        formatter.display_ip_information({"ip": "8.8.8.8"})
        output = recording_console.export_text()
    finally:
        formatter.console = original_console

    assert "8.8.8.8" in output
    assert "Not available" in output


def test_formatter_rejects_non_dictionary_data():
    """Confirm invalid display input shows a simple error."""
    recording_console = Console(record=True, force_terminal=False)
    original_console = formatter.console
    formatter.console = recording_console

    try:
        formatter.display_ip_information(None)
        output = recording_console.export_text()
    finally:
        formatter.console = original_console

    assert "Unable to retrieve IP information" in output
