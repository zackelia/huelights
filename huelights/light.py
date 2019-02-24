""" This module provides the Light class """
import huelights.utils as utils


class Light:
    """ Represents the Lights API object """
    def __init__(self, index, url, data):
        self._index = index
        self._url = url

        self._state = data['state']
        self._name = data['name']
        self._product_name = data['productname']

    def _refresh_state(self):
        """ Refresh the current light state """
        r = utils.get(self._url)

        if r:
            data = r.json()
            self._state = data['state']

    def _update_state(self, payload):
        """ Update the current light state with payload """
        utils.put(f'{self._url}/state', payload)

        self._refresh_state()

    @property
    def index(self):
        """ Index associated with the light in the Bridge """
        return self._index

    @property
    def name(self):
        """ User created name for the light """
        return self._name

    @property
    def product_name(self):
        """ Philips product name of the light """
        return self._product_name

    # State property getters
    @property
    def on(self):
        """ On/Off state of the light """
        self._refresh_state()
        return self._state['on']

    @property
    def brightness(self):
        """  Brightness in range [0-254] """
        self._refresh_state()
        return self._state['bri']

    @property
    def hue(self):
        """ Hue in range [0-65535] """
        self._refresh_state()
        return self._state['hue']

    @property
    def saturation(self):
        """ Saturation in range [0-254] """
        self._refresh_state()
        return self._state['sat']

    @property
    def xy(self):
        """ Color in xy space as [x, y] """
        self._refresh_state()
        return self._state['xy']

    @property
    def temperature(self):
        """ White color temperature in range [154, 500] """
        self._refresh_state()
        return self._state['ct']

    @property
    def alert(self):
        """ Temporary alert effect """
        self._refresh_state()
        return self._state['alert']

    @property
    def effect(self):
        """ Dynamic effect on the light """
        self._refresh_state()
        return self._state['effect']

    # State property setters
    @on.setter
    def on(self, on):
        self._update_state({'on': on})

    @brightness.setter
    def brightness(self, brightness):
        self._update_state({'bri': brightness})

    @hue.setter
    def hue(self, hue):
        self._update_state({'hue': hue})

    @saturation.setter
    def saturation(self, saturation):
        self._update_state({'sat': saturation})

    @xy.setter
    def xy(self, xy):
        self._update_state({'xy': xy})

    @temperature.setter
    def temperature(self, temperature):
        self._update_state({'ct': temperature})

    @alert.setter
    def alert(self, alert):
        self._update_state({'alert': alert})

    @effect.setter
    def effect(self, effect):
        self._update_state({'effect': effect})
