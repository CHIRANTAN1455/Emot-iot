from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.config import MQTT_TOPIC
from app.mqtt_service import MQTTService

app = FastAPI(title="Emot IoT MQTT API", version="1.0.0")
mqtt_service = MQTTService()


class PublishPayload(BaseModel):
    device_id: str = Field(default="emot-device-01")
    status: str = Field(default="online")
    temperature_c: float = Field(default=24.5)
    humidity: float = Field(default=55.0)


@app.on_event("startup")
def startup_event() -> None:
    mqtt_service.start()


@app.on_event("shutdown")
def shutdown_event() -> None:
    mqtt_service.stop()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "topic": MQTT_TOPIC}


@app.post("/publish")
def publish(payload: PublishPayload) -> dict:
    message = {
        "deviceId": payload.device_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": payload.status,
        "temperatureC": payload.temperature_c,
        "humidity": payload.humidity,
    }
    mqtt_service.publish(message)
    return {"published": True, "topic": MQTT_TOPIC, "message": message}


@app.post("/simulator/start")
def start_simulator() -> dict:
    started = mqtt_service.start_simulator(interval_seconds=3.0)
    return {"started": started}


@app.post("/simulator/stop")
def stop_simulator() -> dict:
    stopped = mqtt_service.stop_simulator()
    return {"stopped": stopped}
