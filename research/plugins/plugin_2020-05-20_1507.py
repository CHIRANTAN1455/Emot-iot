"""MQTT plugin: tls_mqtt_handshake (2020-05-20)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20200520_1507 = MQTTPluginHandler("tls_mqtt_handshake", lambda p: p)
