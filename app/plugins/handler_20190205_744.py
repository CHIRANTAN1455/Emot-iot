"""FastAPI MQTT backend plugin — mqtt5_user_properties."""
class BackendMQTTPlugin:
    plugin_id = "mqtt5_user_properties_744"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2019-02-05"}
