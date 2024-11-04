import logging

from .stadtwerkeflensburg import StadtwerkeFlensburg

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
# from homeassistant.exceptions import ConfigEntryNotReady, IntegrationError
# from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed


from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    st_fl = StadtwerkeFlensburg(
        email=entry.data[CONF_USERNAME],
        password=entry.data[CONF_PASSWORD]
    )

    # coordinator = hass.DataUpdateCoordinator(hass, _LOGGER, name=DOMAIN, update_interval=DEFAULT_UPDATE_INTERVAL)

    await st_fl.async_start()
    if not await st_fl.async_login():
        return False

    # await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    # hass.data[DOMAIN][entry.entry_id] = {DATA_COORDINATOR: coordinator}

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


# async def async_reload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
#     await async_unload_entry(hass, config_entry)
#     await async_setup_entry(hass, config_entry)

# async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None):
#     if user_input is not None:
#         # TODO: process user input
#         self.async_set_unique_id(user_id)
#         self._abort_if_unique_id_mismatch()
#         return self.async_update_reload_and_abort(
#             self._get_reconfigure_entry(),
#             data_updates=data,
#         )
#
#     return self.async_show_form(
#         step_id="reconfigure",
#         data_schema=vol.Schema({vol.Required("input_parameter"): str}),
#     )
