"""MQTT plugin: sensor_batch_ingest (2021-05-18)."""
from typing import Any, Callable

class MQTTPluginHandler:
    def __init__(self, name: str, handler: Callable[[dict], Any]) -> None:
        self.name = name
        self._handler = handler

    def on_message(self, topic: str, payload: dict) -> Any:
        return self._handler({"mqtt_topic": topic, **payload})

handler_20210518_2178 = MQTTPluginHandler("sensor_batch_ingest", lambda p: p)
