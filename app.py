"""Main entry point for the NetInfo IP App."""

from src.api_client import get_current_ip_information, get_ip_information
from src.formatter import console, display_ip_information, show_error, show_success
from src.menu import display_menu, get_menu_choice
from src.validators import validate_ip_address


def run_application():
    """Run the menu-driven IP information application until the user exits."""
    console.print("[bold cyan]Welcome to NetInfo IP App[/bold cyan]")

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            data = get_current_ip_information()

            if data:
                show_success("Current public IP information retrieved successfully.")
                display_ip_information(data)

        elif choice == "2":
            ip_address = console.input(
                "[cyan]Enter an IPv4 or IPv6 address: [/cyan]"
            ).strip()

            is_valid, message = validate_ip_address(ip_address)

            if not is_valid:
                show_error(message)
                continue

            show_success(message)
            data = get_ip_information(ip_address)

            if data:
                display_ip_information(data)

        elif choice == "3":
            console.print(
                "[yellow]Thank you for using NetInfo IP App. Goodbye![/yellow]"
            )
            break

        else:
            show_error("Invalid menu choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_application()
