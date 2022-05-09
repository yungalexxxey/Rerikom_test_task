from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    bootstrap_servers=['172.15.1.8:9093'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
