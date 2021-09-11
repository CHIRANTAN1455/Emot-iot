"""FastAPI MQTT backend plugin — mqtt5_user_properties."""
class BackendMQTTPlugin:
    plugin_id = "mqtt5_user_properties_2446"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-09-11"}
