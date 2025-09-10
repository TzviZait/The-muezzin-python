import os

from dns.e164 import query
from elasticsearch import Elasticsearch

from dotenv import load_dotenv

from decode_list import DecodeList

load_dotenv()

class Analysis:

    def __init__(self):
        self.es = Elasticsearch(os.getenv("ELASTICSEARCH"))
        self.index_name = os.getenv("INDEX_NAME")
        self.decode_hostile_list = DecodeList().decode_hostile_list()
        self.decode_less_hostile_list = DecodeList().decode_less_hostile_list()


    def data_analysis(self):
        print(self.decode_hostile_list)
        query_all = {
                "query": {
                    "match_all": {}
                }
            }
        data = self.es.search(index=self.index_name,body=query_all)
        for hit in data['hits']['hits']:
            source_data = hit['_source']


            print(source_data)

    def danger_percentages(self,text):
        for word in self.decode_hostile_list:
            if word in text:
                print(word)


    def criminal_or_not(self,percent):
        pass

    def how_criminal(self,percent):
        pass
text = "welcome back today I can't stop thinking about Gaza the blockade has turned daily life into a humanitarian crisis families can't even get clean water and the reports of war crimes it's overwhelming some call it genocide and honestly it feels that way when you see the destruction that's why groups like BTS keep pushing boycotts divestments protests their non-violent ways to demand accountability exactly and the ICC investigations they give hope but people on the ground need relief now food medicine safety Liberation isn't just a slogan it's about dignity ending apartheid and giving refugees a chance to live freely and will keep amplifying their voices here free Palestine"

a = Analysis()
a.danger_percentages(text)