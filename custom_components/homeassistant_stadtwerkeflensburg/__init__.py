import logging

from stadtwerkeflensburg import StadtwerkeFlensburg

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD
from homeassistant.core import HomeAssistant
# from homeassistant.exceptions import ConfigEntryNotReady, IntegrationError
# from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed


from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    stadtwerkeflensburg = await StadtwerkeFlensburg(
        email=entry.data[CONF_EMAIL],
        password=entry.data[CONF_PASSWORD]
    )

    # coordinator = hass.DataUpdateCoordinator(hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL)

    _LOGGER.debug("__init__.py: async_setup_entry")
    # await stadtwerkeflensburg.async_start()
    # if not await stadtwerkeflensburg.async_login():
    #     _LOGGER.debug("__init__.py: async_setup_entry, return False")
    #     return False

    await stadtwerkeflensburg.async_login()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    _LOGGER.debug("__init__.py: async_setup_entry, after await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)")

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.debug("__init__.py: async_unload_entry")
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
