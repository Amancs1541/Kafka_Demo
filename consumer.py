import json
from confluent_kafka import Consumer
from db_config import get_db_connection, setup_database

setup_database()

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])

print("🟢 Consumer is running and subscribed to 'orders' topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)

        print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (user, item, quantity) VALUES (?, ?, ?)",
            (order["user"], order["item"], order["quantity"])
        )

        conn.commit()
        conn.close()

except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()
