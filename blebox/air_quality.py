"""BleBox air quality entity."""

from homeassistant.components.air_quality import AirQualityEntity

from . import CommonEntity, async_add_blebox

# NOTE: this should be removed once client library uses a semaphore
PARALLEL_UPDATES = 1

# pylint: disable=fixme


# TODO: remove?
async def async_setup_platform(hass, config, async_add, discovery_info=None):
    """Set up a BleBox air quality device."""
    # TODO: coverage
    return await async_add_blebox(
        BleBoxAirQualityEntity, "air_qualities", hass, config, async_add
    )


async def async_setup_entry(hass, config_entry, async_add):
    """Set up a BleBox air quality device."""
    # TODO: coverage
    return await async_add_blebox(
        BleBoxAirQualityEntity, "air_qualities", hass, config_entry.data, async_add,
    )


class BleBoxAirQualityEntity(CommonEntity, AirQualityEntity):
    """Representation of a BleBox air quality feature."""

    @property
    def icon(self):
        """Return the icon."""
        return "mdi:blur"

    @property
    def particulate_matter_0_1(self):
        """Return the particulate matter 0.1 level."""
        return self._feature.pm1

    @property
    def particulate_matter_2_5(self):
        """Return the particulate matter 2.5 level."""
        return self._feature.pm2_5

    @property
    def particulate_matter_10(self):
        """Return the particulate matter 10 level."""
        return self._feature.pm10
