from app.main.lib.es_indexer_base import ESIndexerBase


class ESIndexerTest(ESIndexerBase):
    """
    Unit Test Indexer class
    """

    def __init__(self, name):
        super().__init__(name)

    def get_es_mapping_fields(self):
        return {
            "comment_detail": {"type": "text", "analyzer": "ik_smart", "search_analyzer": "ik_smart"},
            "comment_person": {"type": "keyword"},
            "comment_time": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            "create_time": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            "hosp_id": {"type": "keyword"},
            "id": {"type": "keyword"},
            "star": {"type": "long"},
            "update_time": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            "url": {"type": "text"},
            "vip_tag": {"type": "long"}
        }
