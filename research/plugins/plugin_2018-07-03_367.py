"""MQTT plugin: zigbee2mqtt_integration (2018-07-03)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20180703_367 = MQTTPluginHandler("zigbee2mqtt_integration", lambda p: p)
