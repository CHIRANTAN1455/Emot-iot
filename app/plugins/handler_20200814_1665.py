"""FastAPI MQTT backend plugin — json_payload_validation."""
class BackendMQTTPlugin:
    plugin_id = "json_payload_validation_1665"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-08-14"}
