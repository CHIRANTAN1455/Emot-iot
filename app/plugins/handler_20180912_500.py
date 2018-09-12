"""FastAPI MQTT backend plugin — actuator_command_queue."""
class BackendMQTTPlugin:
    plugin_id = "actuator_command_queue_500"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2018-09-12"}
