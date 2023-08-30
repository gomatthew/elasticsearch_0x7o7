from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:19200")
print(client.info())


es_mapping ={}
client.indices.create(index='test',body=es_mapping)