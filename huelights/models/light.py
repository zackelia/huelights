"""Provide the light model."""
from typing import List

from ..utils import get, put


class Light:
    """A light object."""

    def __init__(self, id, data, url):
        self._state = data["state"]
        self._type = data["type"]
        self._name = data["name"]
        self._model_id = data["modelid"]
        self._manufacturer_name = data["manufacturername"]
        self._product_name = data["productname"]
        self._unique_id = data["uniqueid"]
        self._software_version = data["swversion"]

        self._id = id
        self._url = f"{url}/{id}"

    def _refresh_state(self):
        response = get(self._url)

        if response:
            data = response.json()
            self._state = data["state"]

    def _update_state(self, data):
        put(f"{self._url}/state", data=data)

        self._refresh_state()

    @property
    def type(self) -> str:
        """A fixed name describing the type of light e.g. “Extended color light”."""
        return self._type

    @property
    def name(self) -> str:
        """A unique, editable name given to the light."""
        return self._name

    @property
    def model_id(self) -> str:
        """The hardware model of the light."""
        return self._model_id

    @property
    def manufacturer_name(self) -> str:
        """The manufacturer name."""
        return self._manufacturer_name

    @property
    def product_name(self) -> str:
        """The product name."""
        return self._product_name

    @property
    def unique_id(self) -> str:
        """
        Unique id of the device. The MAC address of the device with a unique endpoint id in the form:
        AA:BB:CC:DD:EE:FF:00:11-XX
        """
        return self._unique_id

    @property
    def software_version(self) -> str:
        """An identifier for the software version running on the light."""
        return self._software_version

    @property
    def on(self) -> bool:
        """On/Off state of the light."""
        self._refresh_state()
        return self._state["on"]

    @property
    def brightness(self) -> int:
        """
        Brightness of the light. This is a scale from the minimum brightness the light is capable of, 1, to the maximum
        capable brightness, 254.
        """
        self._refresh_state()
        return self._state["bri"]

    @property
    def hue(self) -> int:
        """
        Hue of the light. This is a wrapping value between 0 and 65535. Note, that hue/sat values are hardware dependent
        which means that programming two devices with the same value does not guarantee that they will be the same
        color. Programming 0 and 65535 would mean that the light will resemble the color red, 21845 for green and 43690
        for blue.
        """
        self._refresh_state()
        return self._state["hue"]

    @property
    def saturation(self) -> int:
        """Saturation of the light. 254 is the most saturated (colored) and 0 is the least saturated (white)."""
        self._refresh_state()
        return self._state["sat"]

    @property
    def xy(self) -> List[float]:
        """
        The x and y coordinates of a color in CIE color space.

        The first entry is the x coordinate and the second entry is the y coordinate. Both x and y are between 0 and 1.
        Using CIE xy, the colors can be the same on all lamps if the coordinates are within every lamps gamuts (example:
        “xy”:[0.409,0.5179] is the same color on all lamps). If not, the lamp will calculate it’s closest color and use
        that. The CIE xy color is absolute, independent from the hardware.
        """
        self._refresh_state()
        return self._state["xy"]

    @property
    def temperature(self) -> int:
        """The Mired Color temperature of the light. 2012 connected lights are capable of 153 (6500K) to 500 (2000K)."""
        self._refresh_state()
        return self._state["ct"]

    @property
    def alert(self) -> str:
        """
        The alert effect, which is a temporary change to the bulb’s state. This can take one of the following values:
            “none” – The light is not performing an alert effect.
            “select” – The light is performing one breathe cycle.
            “lselect” – The light is performing breathe cycles for 15 seconds or until an "alert": "none" command is
                        received.
        Note that this contains the last alert sent to the light and not its current state. i.e. After the breathe cycle
        has finished the bridge does not reset the alert to “none“.
        """
        self._refresh_state()
        return self._state["alert"]

    @property
    def effect(self) -> str:
        """
        The dynamic effect of the light, can either be “none” or “colorloop”.If set to colorloop, the light will cycle
        through all hues using the current brightness and saturation settings.
        """
        self._refresh_state()
        return self._state["effect"]

    @on.setter
    def on(self, on):
        self._update_state({"on": on})

    @brightness.setter
    def brightness(self, brightness):
        self._update_state({"bri": brightness})

    @hue.setter
    def hue(self, hue: int):
        self._update_state({"hue": hue})

    @saturation.setter
    def saturation(self, saturation):
        self._update_state({"sat": saturation})

    @xy.setter
    def xy(self, xy):
        self._update_state({"xy": xy})

    @temperature.setter
    def temperature(self, temperature):
        self._update_state({"ct": temperature})

    @alert.setter
    def alert(self, alert):
        self._update_state({"alert": alert})

    @effect.setter
    def effect(self, effect):
        self._update_state({"effect": effect})
