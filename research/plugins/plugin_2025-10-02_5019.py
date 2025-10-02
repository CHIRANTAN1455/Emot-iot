"""MQTT plugin: retain_flag_patterns (2025-10-02)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20251002_5019 = MQTTPluginHandler("retain_flag_patterns", lambda p: p)
