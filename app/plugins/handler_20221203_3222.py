"""FastAPI MQTT backend plugin — iot_plugin_registry."""
class BackendMQTTPlugin:
    plugin_id = "iot_plugin_registry_3222"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-12-03"}
