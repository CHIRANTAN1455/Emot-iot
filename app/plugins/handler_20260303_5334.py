"""FastAPI MQTT backend plugin — lorawan_uplink_mqtt."""
class BackendMQTTPlugin:
    plugin_id = "lorawan_uplink_mqtt_5334"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2026-03-03"}
