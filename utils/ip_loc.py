import socket
from urllib.parse import urlparse

import requests
import socks


def trace_proxy_connection(proxy_url):
    # Parse the proxy URL
    parsed = urlparse(f'http://{proxy_url}')
    proxy_host = parsed.hostname
    proxy_port = parsed.port
    username = parsed.username
    password = parsed.password

    # Store the original socket
    original_socket = socket.socket

    # Set up the SOCKS5 proxy
    socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port, username=username, password=password)
    socket.socket = socks.socksocket

    try:
        # Make a request to an IP geolocation service
        response = requests.get('https://ipapi.co/json/')
        data = response.json()

        country = data.get('country_name', 'Unknown')
        city = data.get('city', 'Unknown')
        ip = data.get('ip', 'Unknown')

        return f"Connected via: {country}, {city} (IP: {ip})"
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Reset the default socket
        socket.socket = original_socket
