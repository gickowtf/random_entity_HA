import random
import logging
from datetime import timedelta
from homeassistant.helpers.entity import Entity

DOMAIN = "random_entity"
_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get('name', 'random_entity')
    chance = config.get('chance', 50)
    scan_interval = config.get('scan_interval', 30)  # Standardwert ist 30 Sekunden

    add_entities([RandomEntity(name, chance)], update_before_add=True)

    # Setzen Sie das Scan-Intervall
    global SCAN_INTERVAL
    SCAN_INTERVAL = timedelta(seconds=scan_interval)


class RandomEntity(Entity):
    def __init__(self, name, chance):
        self._name = name
        self._state = None
        self._chance = chance

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        if random.randint(1, 100) <= self._chance:
            self._state = "on"
        else:
            self._state = "off"