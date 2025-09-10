import os

from elasticsearch import Elasticsearch

from dotenv import load_dotenv

from dal import DAL

from data_to_json import DataToJson

load_dotenv()

data = DataToJson()
dal = DAL()




es = Elasticsearch(os.getenv("ELASTICSEARCH"))


#
#
# query = {
#     "query": {
#         "match": {
#             "text": "computer"
#         }
#     }
# }
#
# results = es.search(index=index_name, body=query)
#
# print(f"Found {results['hits']['total']['value']} results.")
# for hit in results['hits']['hits']:
#     print(f"ID: {hit['_id']} - Category: {hit['_source']['category']}")
#     print(f"Text: {hit['_source']['text'][:200]}...\n")  # Print first 200 characters