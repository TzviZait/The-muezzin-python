import os

from dotenv import load_dotenv
from sympy.physics.units import percent

from decode_list import DecodeList

from elasticsearch_index import ElasticsearchIndex

load_dotenv()


class Analysis:

    def __init__(self):
        self.es = ElasticsearchIndex()
        self.index_name = os.getenv("INDEX_NAME")
        self.decode_hostile_list = DecodeList().decode_hostile_list()
        self.decode_less_hostile_list = DecodeList().decode_less_hostile_list()


    def data_analysis(self,dict):
        for k, v in dict.items():
            self.es.es.index(index=self.index_name, id=k, body=v)
        query_all = {
                "query": {
                    "match_all": {}
                }
            }
        data = self.es.es.search(index=self.index_name,body=query_all)
        for hit in data['hits']['hits']:
            source_data = hit['_source']["audio_text"]
            percent = Analysis().danger_percentages(source_data)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"bds_percent":percent}})
            criminal = Analysis().criminal_or_not(percent)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"is_bds":criminal}})
            level = Analysis().how_criminal(percent)
            self.es.es.update(index=self.index_name,id=hit["_id"],body={"doc":{"bds_threat_level":level}})

    def danger_percentages(self,text):
        count = 0
        for word in self.decode_hostile_list:
            if word.lower() in text.lower():
                count += 2
        for word in self.decode_less_hostile_list:
            if word.lower() in text.lower():
                count += 1
        sum = count * len(text.split()) // 100
        return sum


    def criminal_or_not(self,percent):
        if percent > 40:
            return True
        else:
            return False

    def how_criminal(self,percent):
        if percent <= 10:
            return "none"
        elif 10 < percent <= 40:
            return "medium"
        else:
            return "high"

