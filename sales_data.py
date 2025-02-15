# Sales data generation
# The data should look as real life as possible

import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
fake = Faker()

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to generate a single sales transaction
def generate_transaction():
    return {
        "transaction_id": random.randint(1000, 9999),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "store_id": f"Store_{random.randint(1, 10)}",
        "product_id": random.randint(100, 200),
        "product_name": random.choice(["Wireless Headphones", "Smartwatch", "Running Shoes", "Coffee Maker", "Yoga Mat"]),
        "category": random.choice(["Electronics", "Apparel", "Home & Kitchen", "Fitness"]),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 200), 2),
        "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "Cash"]),
        "customer_id": fake.uuid4(),
        "region": random.choice(["West", "East", "North", "South"]),
        "promo_code": random.choice([None, "SUMMER20", "WELCOME10", "FALL15"]),
        "weather_condition": random.choice(["Sunny", "Rainy", "Cloudy", "Snowy"])
    }

# Continuously generate and stream data
try:
    while True:
        transaction = generate_transaction()
        producer.send('sales_topic', transaction)
        logger.info(f"Sent transaction: {transaction}")
        time.sleep(random.uniform(1, 10))  # Random interval between 1 and 10 seconds
except KeyboardInterrupt:
    logger.info("Producer stopped.")
finally:
    producer.flush()
    producer.close()