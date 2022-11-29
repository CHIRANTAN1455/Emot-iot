"""FastAPI MQTT backend plugin — coap_mqtt_bridge."""
class BackendMQTTPlugin:
    plugin_id = "coap_mqtt_bridge_3194"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2022-11-29"}
