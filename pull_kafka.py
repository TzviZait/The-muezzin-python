import datetime
import json
from kafka import KafkaConsumer

from elasticsearch_index import index_es
from push_kafka import PushKafka

from mongoDB import DataToMongo

from gridfs import GridFS

from metadata import Metadata

import base64

class Subscriber:

    def __init__(self,kafka_address,topic_name):
        self.kafka_address = kafka_address
        self.connect = PushKafka()
        self.mongo = DataToMongo()
        self.fs = GridFS(self.mongo.mydb)
        self.metadata = Metadata()


        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',
            group_id='my-group'
        )

    def puller_kafka(self):
        print("jj")
        for message in self.consumer:
            message_val = json.loads(message.value.decode('utf-8'))
            print("mm")
            for k,v in message_val.items():
                index_es(k,message_val)
            self.mongo.send_to_mongo(base64.b64encode(message_val.encode('utf-8')))
            print(message_val)

