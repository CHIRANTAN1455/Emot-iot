"""FastAPI MQTT backend plugin — iot_plugin_registry."""
class BackendMQTTPlugin:
    plugin_id = "iot_plugin_registry_2946"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-07-31"}
