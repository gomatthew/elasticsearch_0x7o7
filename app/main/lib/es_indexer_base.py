import json
from abc import ABC, abstractmethod

from app.main import app, es, rq
from app.main.enum.field_type_enum import FieldTypeEnum
from app.main.enum.filter_type_enum import FilterTypeEnum
from app.main.util.return_value import return_value_201


class ESIndexerBase(ABC):
    def __init__(self, index_name):
        self.index_name = app.config.get('ES_INDEX_PREFIX') + index_name

    def get_es_mapping(self, number_of_shards, number_of_replicas):
        index_fields = self.get_es_mapping_fields()
        mapping = {
            "settings": {
                "number_of_shards": number_of_shards,
                "number_of_replicas": number_of_replicas
            },
            "mappings": {
                "dynamic": False,
                "properties": index_fields
            }
        }

        return mapping

    @abstractmethod
    def get_es_mapping_fields(self):
        return []

    def es_index(self, data: json, refresh=False):
        doc_id = data.get('id')
        es.index(index=self.index_name, document=data, id=doc_id, refresh=refresh)
        return return_value_201("index success")

    def es_search(self, current_page, each_page, sort_by, sort_direction, filters, query_setting):
        sort_setting = {}
        if sort_by and sort_by != '':
            sort_setting = {sort_by: {'order': sort_direction}}
        query = {"track_total_hits": True,  # 1万笔数据以上，加此字段
                 "from": current_page,
                 "size": each_page,
                 "sort": sort_setting,
                 "query": {
                     "bool": {
                         "must": [],  # 必须有
                         "must_not": [],  # 必须没有
                         "should": [],  # 可以有并且需要设定最少符合条件数
                         "filter": self.make_bool_filter(filters, query_setting)  # 不会计算相关性算分
                     },
                 }
                 }
        app.logger.info("es_search [start]: {} {}".format(self.index_name, query))
        results = es.search(index=self.index_name, body=query)
        app.logger.info("es_search [end]: total found - {}".format(results['hits']['total']['value']))
        return results['hits']['total']['value'], results['hits']['hits']

    def make_bool_filter(self, filters, query_setting):
        filter_body = {"bool": {
            "must": [],
            "should": []
        }}
        for k, v in filters.items():
            field_setting = query_setting.get(k)
            query_condition = {"term": {k: v}}
            match field_setting.get("field_type"):
                case FieldTypeEnum.LIST.name:
                    query_condition = {"terms": {k: json.loads(v)}}
                case FieldTypeEnum.RANGE.name:
                    left, right = json.loads(v)
                    if (left and left != '') or (right and right != ''):
                        if left and not right:
                            query_condition = {"gte": left}
                        elif right and right != '':
                            query_condition = {"lte": right}
                        else:
                            query_condition = {"gte": left, "lte": right}
                case FieldTypeEnum.DATETIME_RANGE.name:
                    left, right = json.loads(v)
                    if (left and left != '') or (right and right != ''):
                        if left and not right:
                            # cond = {"gte": left, "time_zone": "Asia/Shanghai"}
                            cond = {"gte": left}
                        elif right and not left:
                            # cond = {"lte": right, "time_zone": "Asia/Shanghai"}
                            cond = {"lte": right}
                        else:
                            # cond = {"gte": left, "lte": right, "time_zone": "Asia/Shanghai"}
                            cond = {"gte": left, "lte": right}
                        query_condition = {"range": {k: cond}}
                case FieldTypeEnum.CONTAIN.name:
                    query_condition = {"match_phrase": {k: v}}
            match field_setting.get('filter_type'):
                case FilterTypeEnum.MUST.name:
                    filter_body['bool']['must'].append(query_condition)
                case _:
                    filter_body['bool']['should'].append(query_condition)

        if len(filter_body['bool']['should']) > 0:
            # 最少匹配一个条件
            filter_body['bool']['minimum_should_match'] = 1
        return filter_body

    def es_delete(self, doc_id: str):
        es.delete(index=self.index_name, id=doc_id)
        return return_value_201("delete success")

    def es_update(self, data: json, refresh=False):
        doc_id = data.get('id')
        es.update(index=self.index_name, id=doc_id, body={"doc": data, "doc_as_upsert": True}, refresh=refresh)
        return return_value_201("update success")

    # def es_update_bulk(self, items, refresh=False):
    #     data = list()
    #     for item in items:
    #         action = {"_op_type": 'update', "_index": self.index_name, "_source": item, "_id": item.get('id')}
    #         data.append(action)
    #     resp = bulk(es, data, index=self.index_name, refresh=refresh)
    #     return resp
    #
    # def es_delete_bulk(self, items, refresh=False):
    #     data = list()
    #     for item in items:
    #         action = {"_op_type": 'delete', "_index": self.index_name, "_source": item, "_id": item.get('id')}
    #         data.append(action)
    #     resp = bulk(es, data, index=self.index_name, refresh=refresh)
    #     return resp

    def create_es_index(self):
        app.logger.info(
            f'creating index:{self.index_name} with {app.config.get("ES_INDEX_SHARDS")} shards and {app.config.get("ES_INDEX_REPLICAS")} replicas.')
        es_mapping = self.get_es_mapping(number_of_shards=app.config.get('ES_INDEX_SHARDS'),
                                         number_of_replicas=app.config.get('ES_INDEX_REPLICAS'))
        es.indices.delete(index=self.index_name, ignore_unavailable=True)
        es.indices.create(index=self.index_name, body=es_mapping)
