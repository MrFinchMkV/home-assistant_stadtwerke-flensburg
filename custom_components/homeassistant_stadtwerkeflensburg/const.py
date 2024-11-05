from datetime import timedelta
from homeassistant.const import Platform

DOMAIN = "stadtwerke_flensburg"
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=5)
PLATFORMS = [Platform.SENSOR]
