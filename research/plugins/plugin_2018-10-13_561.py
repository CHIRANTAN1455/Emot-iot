"""MQTT plugin: json_payload_validation (2018-10-13)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20181013_561 = MQTTPluginHandler("json_payload_validation", lambda p: p)
