"""MQTT plugin: mqtt5_user_properties (2022-07-05)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20220705_2906 = MQTTPluginHandler("mqtt5_user_properties", lambda p: p)
