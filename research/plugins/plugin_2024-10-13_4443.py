"""MQTT plugin: will_message_handling (2024-10-13)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20241013_4443 = MQTTPluginHandler("will_message_handling", lambda p: p)
