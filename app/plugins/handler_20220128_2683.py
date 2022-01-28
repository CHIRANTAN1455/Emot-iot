"""FastAPI MQTT backend plugin — broker_load_balancing."""
class BackendMQTTPlugin:
    plugin_id = "broker_load_balancing_2683"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-01-28"}
