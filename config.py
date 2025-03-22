from dotenv import load_dotenv
import os

load_dotenv()
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "AppsflyerDataStreamingService")
