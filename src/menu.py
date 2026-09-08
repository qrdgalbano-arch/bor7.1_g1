"""Menu display and user input functions for the NetInfo IP App."""

from rich.console import Console

console = Console()


def display_menu():
    """Display the main application menu."""
    console.print("\n[bold cyan]========== NETINFO IP APP ==========[/bold cyan]")
    console.print("[white]1.[/white] Check my current public IP address")
    console.print("[white]2.[/white] Look up a specific IPv4 or IPv6 address")
    console.print("[white]3.[/white] Exit")


def get_menu_choice():
    """Get and return the user's menu selection."""
    return console.input("[cyan]Choose an option (1-3): [/cyan]").strip()
