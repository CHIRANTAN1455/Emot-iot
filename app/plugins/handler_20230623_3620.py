"""FastAPI MQTT backend plugin — json_payload_validation."""
class BackendMQTTPlugin:
    plugin_id = "json_payload_validation_3620"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2023-06-23"}
