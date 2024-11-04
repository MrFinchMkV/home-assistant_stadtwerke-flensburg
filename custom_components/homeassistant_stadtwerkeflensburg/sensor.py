from .stadtwerkeflensburg import StadtwerkeFlensburg
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
# from homeassistant.helpers.update_coordinator import (
#     CoordinatorEntity,
#     DataUpdateCoordinator,
# )
from homeassistant.components.sensor import (
    # SensorDeviceClass,
    SensorEntity,
    # SensorStateClass,
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:

    st_fl = StadtwerkeFlensburg(
        email=entry.data[CONF_USERNAME],
        password=entry.data[CONF_PASSWORD]
    )

    await st_fl.async_start()
    await st_fl.async_login()

    st_fl_sensor = StadtwerkeFlensburgSensor(st_fl)

    entities = []
    entities.append(st_fl_sensor)
    async_add_entities(entities, True)

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([StadtwerkeFlensburgSensor()])


# class StadtwerkeFlensburgSensor(CoordinatorEntity, SensorEntity):
class StadtwerkeFlensburgSensor(SensorEntity):
     """Representation of a Sensor."""

    _attr_name = "Reading"
    # _attr_native_unit_of_measurement = UnitOfEnergy.kWh
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _suggested_display_precision = 1
    _attr_native_value = ""

    def __init__(self, st_fl: StadtwerkeFlensburg):
        self.st_fl = st_fl
        self._attr_native_value = ""

    async def async_update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._attr_native_value = await self.st_fl.async_get_last_meter_reading
