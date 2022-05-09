import requests
import json
import jwt
from kafka import KafkaConsumer


def confirm_message(id: int, status: bool):
    encoded_jwt = jwt.encode({"Token": "AUTH_TOKEN"}, "best_password", algorithm="HS256")
    url = "http://172.15.1.6:8000/api/v1/message_confirmation"
    body = {"message_id": id, "status": status}
    headers = {'Authorization': encoded_jwt}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.text)


def scan_message(msg_id: int, message: str):
    if "абракадабра" in message.lower():
        confirm_message(msg_id, False)
    else:
        confirm_message(msg_id, True)


consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['172.15.1.8:9093'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
for event in consumer:
    scan_message(event.value['message_id'], event.value['message'])
