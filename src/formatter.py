"""Rich-based output formatting for IP information and application messages."""

from rich.console import Console
from rich.table import Table

console = Console()


def show_success(message):
    """Display a success message in green."""
    console.print(f"[green]{message}[/green]")


def show_error(message):
    """Display an error message in red."""
    console.print(f"[red]{message}[/red]")


def _value_or_not_available(data, key):
    """Return a safe value, or 'Not available' when a field is missing."""
    value = data.get(key)

    if value is None or value == "":
        return "Not available"

    return str(value)


def display_ip_information(data):
    """Display IP API data in a readable Rich table."""
    if not isinstance(data, dict):
        show_error("Unable to retrieve IP information at this time.")
        return

    table = Table(
        title="IP Information",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Label", style="cyan", no_wrap=True)
    table.add_column("Information", style="white")

    fields = [
        ("Public IP Address", "ip"),
        ("IP Version", "version"),
        ("ASN", "asn"),
        ("Organization / ISP", "org"),
        ("Hostname", "hostname"),
        ("City", "city"),
        ("Region", "region"),
        ("Country", "country_name"),
        ("Country Code", "country_code"),
        ("Postal Code", "postal"),
        ("Latitude", "latitude"),
        ("Longitude", "longitude"),
        ("Timezone", "timezone"),
        ("UTC Offset", "utc_offset"),
    ]

    for label, key in fields:
        table.add_row(label, _value_or_not_available(data, key))

    console.print(table)
