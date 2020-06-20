"""FastAPI MQTT backend plugin — sensor_batch_ingest."""
class BackendMQTTPlugin:
    plugin_id = "sensor_batch_ingest_1580"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-06-20"}
