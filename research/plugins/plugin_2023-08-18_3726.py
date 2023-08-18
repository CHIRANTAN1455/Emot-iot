"""MQTT plugin: mqtt_qos_telemetry (2023-08-18)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20230818_3726 = MQTTPluginHandler("mqtt_qos_telemetry", lambda p: p)
