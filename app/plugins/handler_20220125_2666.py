"""FastAPI MQTT backend plugin — lorawan_uplink_mqtt."""
class BackendMQTTPlugin:
    plugin_id = "lorawan_uplink_mqtt_2666"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-01-25"}
