"""FastAPI MQTT backend plugin — retain_flag_patterns."""
class BackendMQTTPlugin:
    plugin_id = "retain_flag_patterns_2604"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-12-17"}
