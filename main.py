from data_to_json import DataToJson

from dal import DAL

from push_kafka import PushKafka

dal = DAL("C:/files")
data = DataToJson()
pusher = PushKafka()

if __name__ == "__main__":
    pusher.connect("localhost:9092")
    for dict in data.data_to_dict(dal.dal()):
        print(dict)
        pusher.send_by_topic_name("data",dict)
    pusher.close()
