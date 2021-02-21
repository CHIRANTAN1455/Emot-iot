"""FastAPI MQTT backend plugin — subscribe_pattern_wildcards."""
class BackendMQTTPlugin:
    plugin_id = "subscribe_pattern_wildcards_1991"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-02-21"}
