"""MQTT plugin: actuator_command_queue (2024-10-11)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20241011_4433 = MQTTPluginHandler("actuator_command_queue", lambda p: p)
