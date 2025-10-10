"""FastAPI MQTT backend plugin — publish_retry_backoff."""
class BackendMQTTPlugin:
    plugin_id = "publish_retry_backoff_5028"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2025-10-10"}
