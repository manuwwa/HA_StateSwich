import os
# from homeassistant.helpers.entity import ToggleEntity
from homeassistant.components.switch import SwitchEntity

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([StateSwitch()])

class StateSwitch(SwitchEntity):
    def __init__(self):
        self._is_on = False

    @property
    def name(self):
        """Name of the device."""
        return "Fireplace"

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False
