"""MQTT plugin: lorawan_uplink_mqtt (2020-02-16)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20200216_1355 = MQTTPluginHandler("lorawan_uplink_mqtt", lambda p: p)
