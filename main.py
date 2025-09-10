import os

from data_to_json import DataToJson

from dal import DAL
from my_logger import Logger

from push_kafka import PushKafka

from pull_kafka import Subscriber
from dotenv import load_dotenv
from mongoDB import DataToMongo

from audio_to_text import AudioToText
load_dotenv()
dal = DAL(os.getenv("FILE_PATH"))
data = DataToJson()
pusher = PushKafka()
puller = Subscriber(os.getenv("KAFKA_ADDRESS"),os.getenv("TOPIC_NAME"))
mongo = DataToMongo()
logger = Logger.get_logger()
audio = AudioToText()

if __name__ == "__main__":
    # logger.info("The muazin started")
    # logger.error("ooooopsss data invalid")
    pusher.connect(os.getenv("KAFKA_ADDRESS"))
    for dict in data.data_to_dict(dal.dal()):

        pusher.send_by_topic_name("data",dict)
        mongo.send_to_mongo(dict)


    pusher.close()
    puller.puller_kafka()
