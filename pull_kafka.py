import datetime
import json
from kafka import KafkaConsumer

from elasticsearch_index import ElasticsearchIndex

from push_kafka import PushKafka

from mongoDB import DataToMongo

from gridfs import GridFS

from metadata import Metadata


class Subscriber:

    def __init__(self,kafka_address,topic_name):
        self.kafka_address = kafka_address
        self.connect = PushKafka()
        self.mongo = DataToMongo()
        self.fs = GridFS(self.mongo.mydb)
        self.metadata = Metadata()
        self.es = ElasticsearchIndex()


        self.consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=kafka_address,
            auto_offset_reset='earliest',
            group_id='my-group',
        )

    def puller_kafka(self):
        for message in self.consumer:
            message_val = json.loads(message.value.decode('utf-8'))
            self.es.elastic_index(message_val)
            print("tzvi")

