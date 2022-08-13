"""FastAPI MQTT backend plugin — publish_retry_backoff."""
class BackendMQTTPlugin:
    plugin_id = "publish_retry_backoff_2981"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-08-13"}
