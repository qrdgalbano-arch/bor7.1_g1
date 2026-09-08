"""Functions for retrieving public IP information from ipapi.co."""

import requests

API_BASE_URL = "https://ipapi.co"
REQUEST_TIMEOUT = 10


def _request_ip_information(url):
    """Send an API request and return JSON IP information or None."""
    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={"User-Agent": "NetInfo-IP-App/1.0"}
        )

        if response.status_code != 200:
            print("Unable to retrieve IP information at this time.")
            return None

        data = response.json()

        if isinstance(data, dict) and data.get("error"):
            print(data.get("reason", "Unable to retrieve IP information at this time."))
            return None

        return data

    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")
        return None

    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network and try again.")
        return None

    except requests.exceptions.RequestException:
        print("Unable to retrieve IP information at this time.")
        return None

    except ValueError:
        print("Unable to read the API response.")
        return None


def get_current_ip_information():
    """Retrieve public IP information for the computer running the program."""
    return _request_ip_information(f"{API_BASE_URL}/json/")


def get_ip_information(ip_address):
    """Retrieve public information for a supplied IPv4 or IPv6 address."""
    return _request_ip_information(f"{API_BASE_URL}/{ip_address}/json/")
