"""BleBox switch implementation."""
from homeassistant.components.switch import DEVICE_CLASS_SWITCH, SwitchDevice
from homeassistant.exceptions import PlatformNotReady

from . import BleBoxEntity, async_add_blebox


async def async_setup_entry(hass, config_entry, async_add):
    """Set up a BleBox switch entity."""
    return await async_add_blebox(
        BleBoxSwitchEntity,
        "switches",
        hass,
        config_entry.data,
        async_add,
        PlatformNotReady,
    )


class BleBoxSwitchEntity(BleBoxEntity, SwitchDevice):
    """Representation of a BleBox switch feature."""

    @property
    def device_class(self):
        """Return the device class."""
        types = {
            "relay": DEVICE_CLASS_SWITCH,
        }
        return types[self._feature.device_class]

    @property
    def is_on(self):
        """Return whether switch is on."""
        return self._feature.is_on

    async def async_turn_on(self, **kwargs):
        """Turn on the switch."""
        return await self._feature.async_turn_on()

    async def async_turn_off(self, **kwargs):
        """Turn off the switch."""
        return await self._feature.async_turn_off()
