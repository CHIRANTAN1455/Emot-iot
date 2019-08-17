"""MQTT plugin: heartbeat_keepalive_tuning (2019-08-17)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20190817_1076 = MQTTPluginHandler("heartbeat_keepalive_tuning", lambda p: p)
