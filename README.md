# Random Entity 
![hacs badge](https://img.shields.io/badge/HACS-Default-blue)
![python badge](https://img.shields.io/badge/Made%20with-Python-orange)
![last commit](https://img.shields.io/github/last-commit/gickowtf/random_entity_HA?color=red)
![](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=installs&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.random_entity.total)
Random Entity for Home Assistant HACS

It is a simple integration that outputs entities with the random state **on** or **off**.

The whole thing can be done via the configuration.yaml.

Here is an example:

```
sensor:
  - platform: random_entity
    name: "my_random_sensor"
    chance: 70
    scan_interval: 15
```


| **options** | **settings**  |
|:----------|:----------|
| name    | Name for entity   |
| chance    | The probability, expressed as a percentage, that the entity will return a "True/On" state when polled. For example, a chance of 70 means there's a 70% likelihood the entity will be "On" and a 30% likelihood it will be "Off" each time it's checked.|
| scan_interval    | The time interval, expressed in seconds, between successive checks or polls of the entity's state. For instance, a scan_interval of 15 means that the entity's state will be updated every 15 seconds.|


# License

![github licence](https://img.shields.io/badge/Licence-MIT-orange)
