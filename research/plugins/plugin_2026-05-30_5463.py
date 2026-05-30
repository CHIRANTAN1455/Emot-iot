"""MQTT plugin: tls_mqtt_handshake (2026-05-30)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20260530_5463 = MQTTPluginHandler("tls_mqtt_handshake", lambda p: p)
