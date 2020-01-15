"""FastAPI MQTT backend plugin — retain_flag_patterns."""
class BackendMQTTPlugin:
    plugin_id = "retain_flag_patterns_1293"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-01-15"}
