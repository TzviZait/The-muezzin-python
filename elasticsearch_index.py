from elasticsearch import Elasticsearch


es = Elasticsearch('http://localhost:9200')

def index_es(index_name,dict):

    es_with_options = es.options(ignore_status=400)

    es_with_options.indices.create(index=index_name, body=dict)

