"""FastAPI MQTT backend plugin — will_message_handling."""
class BackendMQTTPlugin:
    plugin_id = "will_message_handling_832"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2019-04-01"}
