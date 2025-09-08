from bson import Binary

from data_to_json import DataToJson

from dal import DAL

from push_kafka import PushKafka

from pull_kafka import Subscriber

from mongoDB import DataToMongo

from bson.binary import Binary

import base64

dal = DAL("C:/files")
data = DataToJson()
pusher = PushKafka()
puller = Subscriber("localhost:9092","data")
mongo = DataToMongo()


if __name__ == "__main__":
    pusher.connect("localhost:9092")
    for dict in data.data_to_dict(dal.dal()):
        for k,v in dict.items():
            v["text_audio"] = base64.b64decode(Binary(mongo.json_for_mongo(dict))).decode('utf-8')
        pusher.send_by_topic_name("data",dict)
    pusher.close()
    puller.puller_kafka()
