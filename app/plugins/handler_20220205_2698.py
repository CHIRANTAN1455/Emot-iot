"""FastAPI MQTT backend plugin — session_persistence."""
class BackendMQTTPlugin:
    plugin_id = "session_persistence_2698"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-02-05"}
