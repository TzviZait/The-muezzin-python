from elasticsearch import Elasticsearch


# es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
es = Elasticsearch('http://localhost:9200')



index_name = "my_dictionary_index"

# Define a simple mapping for your dictionary documents
mapping = {
    "mappings": {
        "properties": {
            "key_field": {"type": "keyword"},  # Example field for a dictionary key
            "value_field": {"type": "text"}   # Example field for a dictionary value
        }
    }
}
def index_es(index_name,dict):

    es_with_options = es.options(ignore_status=400)

    es_with_options.indices.create(index=index_name, body=dict)

