import os

from elasticsearch import Elasticsearch

from dotenv import load_dotenv

from dal import DAL

from data_to_json import DataToJson

load_dotenv()

class ElasticsearchIndex:

    def __init__(self):
        self.es = Elasticsearch(os.getenv("ELASTICSEARCH"))
        self.index_name = os.getenv("INDEX_NAME")
        self.dal = DAL(os.getenv("FILE_PATH"))
        self.data = DataToJson()

    def elastic_index(self):

        index_body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },
            "mappings": {
                "properties": {
                    "file_path": {"type": "text"},
                    "file_name": {"type": "text"},
                    "file_size": {"type": "text"},
                    "creation_file": {"type": "text"},
                    "audio_text": {"type": "text"}
                }
            }
        }

        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name, body=index_body)








