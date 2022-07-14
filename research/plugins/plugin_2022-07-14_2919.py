"""MQTT plugin: lorawan_uplink_mqtt (2022-07-14)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20220714_2919 = MQTTPluginHandler("lorawan_uplink_mqtt", lambda p: p)
