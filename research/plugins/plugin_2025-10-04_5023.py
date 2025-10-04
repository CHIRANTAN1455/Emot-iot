"""MQTT plugin: json_payload_validation (2025-10-04)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20251004_5023 = MQTTPluginHandler("json_payload_validation", lambda p: p)
