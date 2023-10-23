"""MQTT plugin: mqtt5_user_properties (2023-10-23)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20231023_3849 = MQTTPluginHandler("mqtt5_user_properties", lambda p: p)
