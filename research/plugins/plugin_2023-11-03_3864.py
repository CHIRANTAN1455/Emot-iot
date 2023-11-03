"""MQTT plugin: mqtt_qos_telemetry (2023-11-03)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20231103_3864 = MQTTPluginHandler("mqtt_qos_telemetry", lambda p: p)
