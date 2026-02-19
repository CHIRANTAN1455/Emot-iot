"""MQTT experiment: publish_retry_backoff (2026-02-19)."""
import json
from dataclasses import dataclass

@dataclass
class MQTTPublishResult:
    topic: str
    qos: int
    payload_bytes: int

def simulate_mqtt_publish(topic: str, payload: dict, qos: int = 1) -> MQTTPublishResult:
    raw = json.dumps(payload).encode("utf-8")
    return MQTTPublishResult(topic=topic, qos=qos, payload_bytes=len(raw))
