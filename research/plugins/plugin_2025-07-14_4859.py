"""MQTT plugin: topic_hierarchy_design (2025-07-14)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20250714_4859 = MQTTPluginHandler("topic_hierarchy_design", lambda p: p)
