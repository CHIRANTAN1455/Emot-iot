"""MQTT plugin: will_message_handling (2020-07-03)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20200703_1591 = MQTTPluginHandler("will_message_handling", lambda p: p)
