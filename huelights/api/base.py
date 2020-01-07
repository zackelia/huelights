"""Provide the API superclass."""
from ..utils import get


class BaseAPI:
    """Base API functionality."""

    def __init__(self, username, ip=None):
        self._username = username

        if ip:
            self._ip = ip
        else:
            response = get("https://discovery.meethue.com")
            self._ip = response.json()[0]["internalipaddress"]

        self._base_url = f"http://{self._ip}/api/{username}"
