import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_ID, CONF_USERNAME, CONF_PASSWORD

from .const import DOMAIN

class StadtwerkeFlensburgConfigFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def _show_setup_form(self, errors=None):
        """Show the setup form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_USERNAME): str, vol.Required(CONF_PASSWORD): str}
            ),
            errors=errors or {},
        )
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return await self._show_setup_form()

        username = user_input[CONF_USERNAME]
        password = user_input[CONF_PASSWORD]

        await self.async_set_unique_id(username)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=username,
            data={
                CONF_ID: username,
                CONF_USERNAME: username,
                CONF_PASSWORD: password,
            },
        )
