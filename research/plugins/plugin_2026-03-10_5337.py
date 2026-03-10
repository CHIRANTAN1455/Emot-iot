"""MQTT plugin: paho_python_bridge (2026-03-10)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20260310_5337 = MQTTPluginHandler("paho_python_bridge", lambda p: p)
