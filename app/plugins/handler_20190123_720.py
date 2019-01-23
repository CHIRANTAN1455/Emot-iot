"""FastAPI MQTT backend plugin — session_persistence."""
class BackendMQTTPlugin:
    plugin_id = "session_persistence_720"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2019-01-23"}
