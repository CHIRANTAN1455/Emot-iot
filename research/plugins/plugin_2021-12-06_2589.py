"""MQTT plugin: subscribe_pattern_wildcards (2021-12-06)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20211206_2589 = MQTTPluginHandler("subscribe_pattern_wildcards", lambda p: p)
