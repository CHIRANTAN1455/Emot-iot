"""FastAPI MQTT backend plugin — paho_python_bridge."""
class BackendMQTTPlugin:
    plugin_id = "paho_python_bridge_2600"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-12-17"}
