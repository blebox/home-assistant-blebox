"""BleBox sensor entities."""

# pylint: disable=fixme

from homeassistant.const import DEVICE_CLASS_TEMPERATURE, TEMP_CELSIUS
from homeassistant.exceptions import PlatformNotReady
from homeassistant.helpers.entity import Entity

from . import CommonEntity, async_add_blebox


async def async_setup_platform(hass, config, async_add, discovery_info=None):
    """Set up BleBox platform."""
    return await async_add_blebox(
        BleBoxSensorEntity, "sensors", hass, config, async_add, PlatformNotReady
    )


async def async_setup_entry(hass, config_entry, async_add):
    """Set up a BleBox entry."""
    return await async_add_blebox(
        BleBoxSensorEntity,
        "sensors",
        hass,
        config_entry.data,
        async_add,
        PlatformNotReady,
    )


# TODO: create and use constants from blebox_uniapi?
UNIT_MAP = {"celsius": TEMP_CELSIUS}
DEV_CLASS_MAP = {"temperature": DEVICE_CLASS_TEMPERATURE}


class BleBoxSensorEntity(CommonEntity, Entity):
    """Representation of a BleBox sensor feature."""

    @property
    def state(self):
        """Return the state."""
        return self._feature.current

    @property
    def unit_of_measurement(self):
        """Return the unit."""
        return UNIT_MAP[self._feature.unit]

    @property
    def device_class(self):
        """Return the device class."""
        return DEV_CLASS_MAP[self._feature.device_class]
