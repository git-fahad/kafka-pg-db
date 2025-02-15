from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.DEBUG)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: v.encode('utf-8')
)
producer.send('sales_topic', 'Hello, Kafka from Python!')
producer.flush()
producer.close()