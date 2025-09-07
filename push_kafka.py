from kafka import KafkaProducer

from data_to_json import DataToJson

import json

class PushKafka:

    def __init__(self, address: str,file_path) -> None:
        self.address = address
        self.data = DataToJson(file_path)

    def connect(self) -> None:
        self.producer = KafkaProducer(bootstrap_servers=self.address)

    def send_by_topic_name(self, topicName: str) -> None:
        self.producer.send(topicName,json.dumps(self.data.data_to_dict()).encode('utf-8'))

    def close(self) -> None:
        self.producer.close()

# pusher = PushKafka("localhost:9092","C:/files")
# pusher.connect()
# pusher.send_by_topic_name("data")
# pusher.close()