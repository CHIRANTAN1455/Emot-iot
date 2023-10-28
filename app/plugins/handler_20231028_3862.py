"""FastAPI MQTT backend plugin — lorawan_uplink_mqtt."""
class BackendMQTTPlugin:
    plugin_id = "lorawan_uplink_mqtt_3862"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2023-10-28"}
