"""FastAPI MQTT backend plugin — sensor_batch_ingest."""
class BackendMQTTPlugin:
    plugin_id = "sensor_batch_ingest_5191"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2025-12-30"}
