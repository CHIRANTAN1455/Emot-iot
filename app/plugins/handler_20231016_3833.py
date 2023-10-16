"""FastAPI MQTT backend plugin — broker_load_balancing."""
class BackendMQTTPlugin:
    plugin_id = "broker_load_balancing_3833"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2023-10-16"}
