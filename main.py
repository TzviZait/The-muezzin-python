
from data_to_json import DataToJson

from dal import DAL
from my_logger import Logger

from push_kafka import PushKafka

from pull_kafka import Subscriber

from mongoDB import DataToMongo

import my_logger

dal = DAL("C:/files")
data = DataToJson()
pusher = PushKafka()
puller = Subscriber("localhost:9092","data")
mongo = DataToMongo()
logger = Logger.get_logger()

if __name__ == "__main__":
    # logger.info("The muazin started")
    # logger.error("ooooopsss data invalid")
    pusher.connect("localhost:9092")
    for dict in data.data_to_dict(dal.dal()):
        pusher.send_by_topic_name("data",dict)

        mongo.send_to_mongo(dict)

    pusher.close()
    puller.puller_kafka()
