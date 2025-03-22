from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    group_id='appsflyer-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print(f"👂 Listening to topic '{KAFKA_TOPIC}'...")

for msg in consumer:
    print("📬 Received event from Kafka:")
    print(json.dumps(msg.value, indent=2))
