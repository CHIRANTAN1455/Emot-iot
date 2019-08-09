"""MQTT plugin: paho_python_bridge (2019-08-09)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20190809_1059 = MQTTPluginHandler("paho_python_bridge", lambda p: p)
