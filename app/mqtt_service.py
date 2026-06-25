import json
import random
import threading
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

from app.config import MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_CLIENT_PREFIX, MQTT_TOPIC


class MQTTService:
    def __init__(self) -> None:
        client_id = f"{MQTT_CLIENT_PREFIX}-api-{random.randint(1000, 9999)}"
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self._simulator_thread = None
        self._simulator_stop_event = threading.Event()

    def start(self) -> None:
        self.client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, keepalive=60)
        self.client.loop_start()

    def stop(self) -> None:
        self.stop_simulator()
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, payload: dict) -> None:
        self.client.publish(MQTT_TOPIC, json.dumps(payload), qos=1)

    def start_simulator(self, interval_seconds: float = 3.0) -> bool:
        if self._simulator_thread and self._simulator_thread.is_alive():
            return False

        self._simulator_stop_event.clear()

        def run() -> None:
            while not self._simulator_stop_event.is_set():
                telemetry = {
                    "deviceId": f"{MQTT_CLIENT_PREFIX}-device-01",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "temperatureC": round(18 + random.random() * 12, 2),
                    "humidity": round(30 + random.random() * 50, 2),
                    "battery": round(50 + random.random() * 50, 1),
                    "motionDetected": random.random() > 0.75,
                }
                self.publish(telemetry)
                time.sleep(interval_seconds)

        self._simulator_thread = threading.Thread(target=run, daemon=True)
        self._simulator_thread.start()
        return True

    def stop_simulator(self) -> bool:
        if not self._simulator_thread or not self._simulator_thread.is_alive():
            return False
        self._simulator_stop_event.set()
        self._simulator_thread.join(timeout=2)
        return True

    def _on_connect(self, client: mqtt.Client, userdata, flags, reason_code, properties) -> None:
        if reason_code == 0:
            print(f"[mqtt] connected to {MQTT_BROKER_HOST}:{MQTT_BROKER_PORT}")
            client.subscribe(MQTT_TOPIC)
            print(f"[mqtt] subscribed to {MQTT_TOPIC}")
        else:
            print(f"[mqtt] connect failed: {reason_code}")

    def _on_message(self, client: mqtt.Client, userdata, message: mqtt.MQTTMessage) -> None:
        try:
            decoded = json.loads(message.payload.decode("utf-8"))
        except Exception:
            decoded = message.payload.decode("utf-8", errors="replace")
        print(f"[mqtt] received on {message.topic}: {decoded}")

    def _on_disconnect(self, client: mqtt.Client, userdata, disconnect_flags, reason_code, properties) -> None:
        print(f"[mqtt] disconnected: {reason_code}")
