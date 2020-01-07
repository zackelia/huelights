"""Provide the lights API."""
from typing import List

from .base import BaseAPI
from ..models import Light
from ..utils import get, delete


class LightsAPI(BaseAPI):
    """API for interacting with lights."""

    def __init__(self, username, ip=None):
        super().__init__(username, ip)
        self._lights = f"{self._base_url}/lights"

    def get_lights(self) -> List[Light]:
        """Gets a list of all lights that have been discovered by the bridge.

        Returns:
            A list of all lights in the system.
        """
        response = get(f"{self._lights}")

        lights = [
            Light(index, data, self._lights) for index, data in response.json().items()
        ]

        return lights

    def delete_lights(self, light: Light) -> None:
        """Deletes a light from the bridge.

        Args:
            light: The light to delete

        """
        delete(f"{self._lights}/{light._id}")
