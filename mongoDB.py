import pymongo


class DAL:
    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myclient["the_muezzin"]



    def send(self,colName,data):
        mycol = self.mydb[colName]
        mycol.insert_one(data)
