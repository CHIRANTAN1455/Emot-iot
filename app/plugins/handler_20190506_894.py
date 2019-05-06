"""FastAPI MQTT backend plugin — coap_mqtt_bridge."""
class BackendMQTTPlugin:
    plugin_id = "coap_mqtt_bridge_894"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2019-05-06"}
