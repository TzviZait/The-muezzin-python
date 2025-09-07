import datetime
import json
from kafka import KafkaConsumer
from push_kafka import PushKafka

class Subscriber:

    def __init__(self,kafka_address,file_path,topic_name):
        self.kafka_address = kafka_address
        self.connect = PushKafka(file_path).connect()

        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',
            group_id='my-group'
        )

        # i = 0
        for message in self.consumer:

            message_val = json.loads(message.decode('utf-8'))
            print(message_val)
            # if message.topic == topic_name:
            #     self.kafka_pusher.send_by_topic_name(target_topic_name_1,message_val)
            # else:
            #     self.kafka_pusher.send_by_topic_name(target_topic_name_2,message_val)
            # print(F"messeage {i} sended {message_val}")
            # i += 1

data = Subscriber("localhost:9092","C:/files","data")
print(data)