import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "test.mosquitto.org")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "emot-iot/device/data")
MQTT_CLIENT_PREFIX = os.getenv("MQTT_CLIENT_PREFIX", "emot")
