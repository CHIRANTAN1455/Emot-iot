"""MQTT plugin: publish_retry_backoff (2018-10-15)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20181015_566 = MQTTPluginHandler("publish_retry_backoff", lambda p: p)
