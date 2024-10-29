from datetime import timedelta

# from homeassistant.components.sensor import (
#     SensorDeviceClass,
#     SensorStateClass,
# )

DOMAIN = "stadtwerke_flensburg"
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=5)
PLATFORMS = ["sensor"]
