# Emot IoT FastAPI + MQTT

A lightweight Python FastAPI backend for MQTT-based IoT device communication.

## Features

- FastAPI endpoints to publish device payloads
- MQTT subscriber running inside the API service
- Built-in telemetry simulator (start/stop by API)
- Environment-based broker and topic configuration

## Quick Start

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment template:

   ```bash
   cp .env.example .env
   ```

4. Run the API:

   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `GET /health`: service status and MQTT topic
- `POST /publish`: publish one payload to MQTT topic
- `POST /simulator/start`: start periodic telemetry publishing
- `POST /simulator/stop`: stop periodic telemetry publishing

## Example Publish Request

```bash
curl -X POST http://127.0.0.1:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "device_id": "emot-device-01",
    "status": "online",
    "temperature_c": 24.2,
    "humidity": 51.3
  }'
```

## Environment Variables

- `MQTT_BROKER_HOST`: broker host, e.g. `test.mosquitto.org`
- `MQTT_BROKER_PORT`: broker port, e.g. `1883`
- `MQTT_TOPIC`: topic used by the service
- `MQTT_CLIENT_PREFIX`: client ID prefix

## Notes

- For production, use broker authentication and TLS (`8883`).
- The public test broker is useful for development, not for private data.
