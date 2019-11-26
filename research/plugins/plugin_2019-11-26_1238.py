"""MQTT plugin: mqtt_sn_gateway_research (2019-11-26)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20191126_1238 = MQTTPluginHandler("mqtt_sn_gateway_research", lambda p: p)
