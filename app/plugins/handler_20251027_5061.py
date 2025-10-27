"""FastAPI MQTT backend plugin — paho_python_bridge."""
class BackendMQTTPlugin:
    plugin_id = "paho_python_bridge_5061"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2025-10-27"}
