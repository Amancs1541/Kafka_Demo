# Kafka Producer-Consumer Example

This project demonstrates a simple **Kafka producer-consumer** workflow using a Kafka cluster running in Docker.

---

## Setup and Usage

### 1. Start Kafka Cluster

To run the Kafka cluster, use Docker Compose:

```bash
docker compose up -d
```
⚠️ Ensure the cluster is running before proceeding. You can check container status using:
```bash
python producer.py
```

After producing messages, start the consumer to read them:
```bash
python consumer.py
```
