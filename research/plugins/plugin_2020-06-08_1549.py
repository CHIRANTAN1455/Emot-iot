"""MQTT plugin: mqtt5_user_properties (2020-06-08)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20200608_1549 = MQTTPluginHandler("mqtt5_user_properties", lambda p: p)
