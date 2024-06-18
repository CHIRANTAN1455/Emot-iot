"""MQTT plugin: mqtt_sn_gateway_research (2024-06-18)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20240618_4251 = MQTTPluginHandler("mqtt_sn_gateway_research", lambda p: p)
