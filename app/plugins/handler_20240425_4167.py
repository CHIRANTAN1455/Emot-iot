"""FastAPI MQTT backend plugin — will_message_handling."""
class BackendMQTTPlugin:
    plugin_id = "will_message_handling_4167"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2024-04-25"}
