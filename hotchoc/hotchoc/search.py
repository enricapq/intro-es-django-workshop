from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
# elasticsearch_dsl 6.2 renamed DocType to Document
from elasticsearch_dsl import Document, Text, Date, Search
from . import models

connections.create_connection()

def search(suggester):
    s = Search().filter('term', suggester=suggester)
    response = s.execute()
    return response  # return a list of hot chocolate stores

# ./manage.py shell
# search()

def bulk_indexing():
    HotChocStoreIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(hc.indexing() for hc in models.HotChocStore.objects.all().iterator()))

class HotChocStoreIndex(Document):
    location = Text()
    suggester = Text()
    created_at = Date()
    name = Text()
    description = Text()

    class Meta:
        index = 'hotchocstore-index'
        name = 'hotchocstore-index'

    # Workaround for https://github.com/elastic/elasticsearch-dsl-py/issues/953
    # elasticsearch-dsl 6.3.1 with elasticsearch 6.3.1
    # elasticsearch_dsl.exceptions.ValidationException: You cannot write to a wildcard index.
    class Index:
        index = 'hotchocstore-index'
        name = 'hotchocstore-index'
