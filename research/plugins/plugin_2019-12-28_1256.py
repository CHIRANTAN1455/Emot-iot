"""MQTT plugin: publish_retry_backoff (2019-12-28)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20191228_1256 = MQTTPluginHandler("publish_retry_backoff", lambda p: p)
