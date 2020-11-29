"""FastAPI MQTT backend plugin — broker_load_balancing."""
class BackendMQTTPlugin:
    plugin_id = "broker_load_balancing_1832"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-11-29"}
