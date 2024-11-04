from .stadtwerkeflensburg import StadtwerkeFlensburg
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, UnitOfEnergy

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
# from homeassistant.helpers.update_coordinator import (
#     CoordinatorEntity,
#     DataUpdateCoordinator,
# )
from homeassistant.components.sensor import SensorEntity

from homeassistant.components.sensor.const import (
    SensorDeviceClass,
    SensorStateClass
)

from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from .const import DOMAIN
import logging
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities
) -> None:

    # st_fl = StadtwerkeFlensburg(
    #     email=entry.data[CONF_EMAIL],
    #     password=entry.data[CONF_PASSWORD]
    # )
    #
    # await st_fl.async_start()
    # await st_fl.async_login()
    #
    # st_fl_sensor = StadtwerkeFlensburgSensor(st_fl)

    # entities = []
    # entities.append(st_fl_sensor)
    # async_add_entities(entities)

    _LOGGER.debug("sensor.py: async_setup_entry")
    test_sensor = StadtwerkeFlensburgSensor(entry)
    async_add_entities([test_sensor], True)



# class StadtwerkeFlensburgSensor(CoordinatorEntity, SensorEntity):
class StadtwerkeFlensburgSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Reading"
    _attr_device_class = SensorDeviceClass.ENERGY
    _attr_state_class = SensorStateClass.TOTAL_INCREASING
    _attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR

    # def __init__(self, st_fl: StadtwerkeFlensburg):
    def __init__(self, entry: ConfigEntry):
        _LOGGER.debug("sensor.py: StadtwerkeFlensburg, __init__")
        self._attr_unique_id = entry.entry_id
        self._attr_device_info = DeviceInfo(
            name="Stadtwerke Flensburg",
            identifiers={(DOMAIN, entry.entry_id)},
            entry_type=DeviceEntryType.SERVICE,
        )
        # self.st_fl = st_fl
        # self._attr_native_value = ""

    async def async_update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        _LOGGER.debug("sensor.py: StadtwerkeFlensburg, async_update")
        self._state = 25
        # self._attr_native_value = await self.st_fl.async_get_last_meter_reading

    @property
    def state(self):
        _LOGGER.debug("sensor.py: StadtwerkeFlensburg, state")
        return self._state
