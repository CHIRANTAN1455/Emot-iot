"""MQTT plugin: coap_mqtt_bridge (2023-06-21)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20230621_3608 = MQTTPluginHandler("coap_mqtt_bridge", lambda p: p)
