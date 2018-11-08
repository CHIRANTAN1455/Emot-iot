"""MQTT plugin: device_shadow_sync (2018-11-08)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20181108_585 = MQTTPluginHandler("device_shadow_sync", lambda p: p)
