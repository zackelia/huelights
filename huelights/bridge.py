"""Provide the bridge class."""
from .api import LightsAPI


class Bridge(LightsAPI):
    """Bridge that has functionality of all endpoints."""

    def __init__(self, username, ip=None):
        super().__init__(username, ip)
