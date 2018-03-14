"""FastAPI MQTT backend plugin — device_shadow_sync."""
class BackendMQTTPlugin:
    plugin_id = "device_shadow_sync_125"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2018-03-14"}
