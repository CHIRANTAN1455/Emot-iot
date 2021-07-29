"""MQTT plugin: topic_hierarchy_design (2021-07-29)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20210729_2352 = MQTTPluginHandler("topic_hierarchy_design", lambda p: p)
