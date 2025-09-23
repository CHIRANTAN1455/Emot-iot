"""MQTT plugin: sensor_batch_ingest (2025-09-23)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20250923_5007 = MQTTPluginHandler("sensor_batch_ingest", lambda p: p)
