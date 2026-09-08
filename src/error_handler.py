"""Error handling helpers for API requests and API response data."""

import requests


def handle_request_exception(error):
    """Print a user-friendly message for a request-related error."""
    if isinstance(error, requests.exceptions.Timeout):
        print("The request took too long. Please try again.")

    elif isinstance(error, requests.exceptions.ConnectionError):
        print("No internet connection. Please check your network and try again.")

    else:
        print("Unable to retrieve IP information at this time.")


def validate_api_response(data):
    """Return valid API data or None when the response is invalid or an API error."""
    if not isinstance(data, dict):
        print("Unable to retrieve IP information at this time.")
        return None

    if data.get("error"):
        reason = data.get("reason")

        if reason:
            print(reason)
        else:
            print("Unable to retrieve IP information at this time.")

        return None

    return data
