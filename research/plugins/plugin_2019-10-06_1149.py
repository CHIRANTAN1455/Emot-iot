"""MQTT plugin: zigbee2mqtt_integration (2019-10-06)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20191006_1149 = MQTTPluginHandler("zigbee2mqtt_integration", lambda p: p)
