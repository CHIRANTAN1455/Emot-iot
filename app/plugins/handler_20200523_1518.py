"""FastAPI MQTT backend plugin — mqtt_qos_telemetry."""
class BackendMQTTPlugin:
    plugin_id = "mqtt_qos_telemetry_1518"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-05-23"}
