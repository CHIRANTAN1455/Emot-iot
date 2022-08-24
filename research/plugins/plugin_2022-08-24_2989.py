"""MQTT plugin: zigbee2mqtt_integration (2022-08-24)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20220824_2989 = MQTTPluginHandler("zigbee2mqtt_integration", lambda p: p)
