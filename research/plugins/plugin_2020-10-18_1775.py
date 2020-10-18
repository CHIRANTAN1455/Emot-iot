"""MQTT plugin: will_message_handling (2020-10-18)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20201018_1775 = MQTTPluginHandler("will_message_handling", lambda p: p)
