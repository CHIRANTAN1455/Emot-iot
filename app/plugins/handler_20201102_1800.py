"""FastAPI MQTT backend plugin — topic_hierarchy_design."""
class BackendMQTTPlugin:
    plugin_id = "topic_hierarchy_design_1800"

    def handle(self, message: dict) -> dict:
        return {"plugin": self.plugin_id, "deviceId": message.get("deviceId", "unknown"), "date": "2020-11-02"}
