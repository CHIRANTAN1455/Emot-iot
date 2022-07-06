"""MQTT plugin: edge_gateway_buffer (2022-07-06)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20220706_2909 = MQTTPluginHandler("edge_gateway_buffer", lambda p: p)
