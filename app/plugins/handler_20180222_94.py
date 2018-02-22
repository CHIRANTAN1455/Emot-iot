"""FastAPI MQTT backend plugin — iot_plugin_registry."""
class BackendMQTTPlugin:
    plugin_id = "iot_plugin_registry_94"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2018-02-22"}
