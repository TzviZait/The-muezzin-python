import pymongo

from gridfs import GridFS


class DataToMongo:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["the_muezzin"]
        self.mycol = self.mydb["data"]
        self.fs = GridFS(self.mydb)

    def send_to_mongo(self,data):
        for k,v in data.items():
            file_path = v["file_path"]
            filename = v["file_name"]
            with open(file_path, 'rb') as f:
                file_id = self.fs.put(f, filename=filename, content_type='audio/wav')
            self.mycol.insert_one({k:file_id})

