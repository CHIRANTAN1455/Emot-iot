"""MQTT plugin: will_message_handling (2018-03-14)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20180314_119 = MQTTPluginHandler("will_message_handling", lambda p: p)
