""" This module provides the Bridge class """
import huelights.utils as utils
from huelights.light import Light


class Bridge:
    """ Represents the Bridge """

    def __init__(self, username, ip=None):
        self._username = username

        if ip:
            self._ip = ip

        else:
            r = utils.get("https://discovery.meethue.com")
            self._ip = r.json()[0]["internalipaddress"]

        self._url = f"http://{self._ip}"

    def get_lights(self):
        """ Get list of all Light objects """
        r = utils.get(f"{self._url}/api/{self._username}/lights")

        lights = []

        for index, body in r.json().items():
            light = Light(
                int(index), f"{self._url}/api/{self._username}/lights/{index}", body
            )
            lights.append(light)

        return lights

    def get_light(self, index):
        """ Get a light object with index """
        r = utils.get(f"{self._url}/api/{self._username}/lights/{index}")

        light = Light(
            int(index), f"{self._url}/api/{self._username}/lights/{index}", r.json()
        )

        return light
