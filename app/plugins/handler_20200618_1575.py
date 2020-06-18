"""FastAPI MQTT backend plugin — edge_gateway_buffer."""
class BackendMQTTPlugin:
    plugin_id = "edge_gateway_buffer_1575"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-06-18"}
