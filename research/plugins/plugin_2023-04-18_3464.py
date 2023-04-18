"""MQTT plugin: publish_retry_backoff (2023-04-18)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20230418_3464 = MQTTPluginHandler("publish_retry_backoff", lambda p: p)
