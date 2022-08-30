"""MQTT plugin: retain_flag_patterns (2022-08-30)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20220830_2995 = MQTTPluginHandler("retain_flag_patterns", lambda p: p)
