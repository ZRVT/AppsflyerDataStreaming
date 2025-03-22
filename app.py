from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
from config import KAFKA_BROKER, KAFKA_TOPIC

app = Flask(__name__)
sent_messages = []  # 🧠 Local store for sent events

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.route("/event", methods=["POST"])
def receive_event():
    data = request.get_json(force=True)
    producer.send(KAFKA_TOPIC, value=data)
    producer.flush()
    sent_messages.append(data)  # 👈 Store locally
    print(f"✅ Sent to Kafka: {data}")
    return jsonify({"status": "sent", "data": data}), 200

@app.route("/events", methods=["GET"])
def list_sent_events():
    return jsonify(sent_messages), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
