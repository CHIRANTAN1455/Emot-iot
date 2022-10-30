"""MQTT plugin: actuator_command_queue (2022-10-30)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20221030_3122 = MQTTPluginHandler("actuator_command_queue", lambda p: p)
