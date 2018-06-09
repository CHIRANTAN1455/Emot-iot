"""MQTT plugin: lorawan_uplink_mqtt (2018-06-09)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20180609_320 = MQTTPluginHandler("lorawan_uplink_mqtt", lambda p: p)
