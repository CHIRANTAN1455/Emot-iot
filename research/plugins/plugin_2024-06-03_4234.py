"""MQTT plugin: iot_plugin_registry (2024-06-03)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20240603_4234 = MQTTPluginHandler("iot_plugin_registry", lambda p: p)
