"""MQTT plugin: retain_flag_patterns (2023-01-08)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20230108_3271 = MQTTPluginHandler("retain_flag_patterns", lambda p: p)
