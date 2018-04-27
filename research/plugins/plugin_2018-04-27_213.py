"""MQTT plugin: topic_hierarchy_design (2018-04-27)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20180427_213 = MQTTPluginHandler("topic_hierarchy_design", lambda p: p)
