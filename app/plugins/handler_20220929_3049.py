"""FastAPI MQTT backend plugin — subscribe_pattern_wildcards."""
class BackendMQTTPlugin:
    plugin_id = "subscribe_pattern_wildcards_3049"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-09-29"}
