"""MQTT plugin: topic_hierarchy_design (2021-11-25)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20211125_2582 = MQTTPluginHandler("topic_hierarchy_design", lambda p: p)
