"""MQTT plugin: heartbeat_keepalive_tuning (2021-05-31)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20210531_2226 = MQTTPluginHandler("heartbeat_keepalive_tuning", lambda p: p)
