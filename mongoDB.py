import os

import pymongo

from gridfs import GridFS

from dotenv import load_dotenv

load_dotenv()

class DataToMongo:
    def __init__(self):
        self.myclient = pymongo.MongoClient(os.getenv("MONGODB_CLIENT"))
        self.mydb = self.myclient[os.getenv("MONGODB_DB")]
        self.mycol = self.mydb[os.getenv("MONGODB_COLUMN")]
        self.fs = GridFS(self.mydb)

    def send_to_mongo(self,data):
        for k,v in data.items():
            file_path = v["file_path"]
            filename = v["file_name"]
            with open(file_path, 'rb') as f:
                file_id = self.fs.put(f, filename=filename, content_type='audio/wav')
            self.mycol.insert_one({k:file_id})

