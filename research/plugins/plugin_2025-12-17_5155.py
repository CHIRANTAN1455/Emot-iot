"""MQTT plugin: backend_message_router (2025-12-17)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20251217_5155 = MQTTPluginHandler("backend_message_router", lambda p: p)
