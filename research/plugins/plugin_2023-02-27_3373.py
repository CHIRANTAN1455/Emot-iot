"""MQTT plugin: broker_load_balancing (2023-02-27)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20230227_3373 = MQTTPluginHandler("broker_load_balancing", lambda p: p)
