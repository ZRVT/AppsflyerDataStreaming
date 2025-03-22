#!/bin/bash
echo "⏳ Waiting for Kafka at $KAFKA_BROKER..."

host=$(echo $KAFKA_BROKER | cut -d: -f1)
port=$(echo $KAFKA_BROKER | cut -d: -f2)

while ! (echo > /dev/tcp/$host/$port) >/dev/null 2>&1; do
  echo "❌ Kafka not available yet at $host:$port..."
  sleep 2
done

echo "✅ Kafka is ready!"
exec python app.py
