from kafka import KafkaProducer

from data_to_json import DataToJson

import json

class PushKafka:

    def __init__(self) -> None:
        pass
    def connect(self,address) -> None:
        self.producer = KafkaProducer(bootstrap_servers=address)

    def send_by_topic_name(self, topicName,message) -> None:
        self.producer.send(topicName,json.dumps(message).encode('utf-8'))

    def close(self) -> None:
        self.producer.close()

data = DataToJson("C:/files").data_to_dict()
pusher = PushKafka()
pusher.connect("localhost:9092")
for message,value in data.items():
    # print(message,value)
    pusher.send_by_topic_name("data",{message:value})
pusher.close()