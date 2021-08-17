"""FastAPI MQTT backend plugin — coap_mqtt_bridge."""
class BackendMQTTPlugin:
    plugin_id = "coap_mqtt_bridge_2389"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2021-08-17"}
