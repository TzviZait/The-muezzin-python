import pymongo


class DataToMongo:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["the_muezzin"]
        self.mycol = self.mydb["data"]

    def send_to_mongo(self,data):

        self.mycol.insert_one(data)

    def json_for_mongo(self,data):
        for k, v in data.items():
            with open(v["file_path"], "rb") as f:
                file_id = f.read()
                return file_id
