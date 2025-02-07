"""MQTT plugin: device_shadow_sync (2025-02-07)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20250207_4633 = MQTTPluginHandler("device_shadow_sync", lambda p: p)
