"""FastAPI MQTT backend plugin — json_payload_validation."""
class BackendMQTTPlugin:
    plugin_id = "json_payload_validation_2493"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-10-02"}
