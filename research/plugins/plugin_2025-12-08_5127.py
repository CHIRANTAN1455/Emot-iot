"""MQTT plugin: lorawan_uplink_mqtt (2025-12-08)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20251208_5127 = MQTTPluginHandler("lorawan_uplink_mqtt", lambda p: p)
