"""FastAPI MQTT backend plugin — broker_load_balancing."""
class BackendMQTTPlugin:
    plugin_id = "broker_load_balancing_2775"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-03-21"}
