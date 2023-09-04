import json
import pandas as pd
from traceback import format_exc
from app.main import rq, app, es
from app.main.lib.es_indexer_factory import ESIndexerFactory
from app.main.util.return_value import return_value_200, return_value_201, return_value_400, return_value_500
from app.main.enum.es_operation_enum import ESOperationEnum
from app.main.util.Util import redis_balance, transfer_datetime, get_current_datetime
from elasticsearch.helpers import bulk


def index_data(data, index_name, operation='index', refresh=False):
    """
    Create or update index data.
    """
    try:
        es_indexer = ESIndexerFactory.create_indexer(index_name)
        resp, status = validate_data(data)
        if status == 400:
            return resp, status
        data = resp.get('data')
        if len(data) > 1:
            queue = redis_balance(app.config.get('BALANCE_KEY'))
            app.logger.info(f'🟢 bulk - {operation} - {es_indexer.index_name} - {len(data)} items with queue:{queue}.')
            es_op_bulk.queue(index_name=es_indexer.index_name, op=operation, items=data, refresh=refresh, queue=queue)
            return return_value_200(message=f'{operation} accept')
        else:
            data = data[0]
        match operation.upper():
            case ESOperationEnum.INDEX.name:
                start_time = get_current_datetime()
                queue = redis_balance(app.config.get('BALANCE_KEY'))
                app.logger.info(f'🟢 {operation} {es_indexer.index_name} single data , queue:{queue}')
                es_index.queue(item=data, index_name=index_name, refresh=refresh, queue=queue)
                app.logger.info(
                    f'🟢 {operation} done with code:{status},spending time:{get_current_datetime() - start_time} \
                    seconds.')
                return return_value_200("index accept")
            case ESOperationEnum.UPDATE.name:
                start_time = get_current_datetime()
                queue = redis_balance(app.config.get('BALANCE_KEY'))
                app.logger.info(f'🟢 {operation} {es_indexer.index_name} single data , queue:{queue}')
                es_update.queue(data, index_name, refresh=refresh, queue=queue)
                app.logger.info(
                    f'🟢 {operation} done with code:{status},spending time:{get_current_datetime() - start_time} \
                    seconds.')
                return return_value_201("update accept")
    except BaseException as e:
        app.logger.error(format_exc())
        app.logger.error(e)
        return return_value_500("Server Error.")


def delete_data(data, index_name, refresh=False):
    start_time = get_current_datetime()
    es_indexer = ESIndexerFactory.create_indexer(index_name)
    if isinstance(data, str):
        data = json.loads(data)
    _ids = data.get('ids')
    delete_action = list()
    if not _ids:
        return return_value_400("id不能为空")
    if len(_ids) > 1:
        for _id in _ids:
            action = {"_op_type": 'delete', "_index": es_indexer.index_name, "_id": _id}
            # app.logger.info(item.get('id'))
            delete_action.append(action)
        resp = bulk(es, delete_action, index=es_indexer.index_name, refresh=refresh, raise_on_error=True)
        if resp[0] == len(_ids):
            app.logger.info(
                f'🟢 Delete Success, data size : {len(data)} , spend time : {get_current_datetime() - start_time}')
            return return_value_201("Delete Success")
        else:
            app.logger.error(f'🔴 Delete Failed, info:{resp}')
            return return_value_500("delete not success")
    resp, status = es_indexer.es_delete(_ids[0])
    return resp, status


def search_data(params, index_name, query_fields, query_setting):
    each_page = int(params.get('eachPage', 10))
    current_page = int(params.get('currentPage', 0))
    sort_by = params.get('sortBy', 'id')
    sort_direction = params.get('sortDirection', 'desc')
    filters = {}

    if each_page > app.config.get("MAX_QUERY_RESULTS"):
        return return_value_400(f"查询接口限制最大查询{app.config.get('MAX_QUERY_RESULTS')}")

    intersection = params.keys() & query_fields.keys()
    for inter in intersection:
        filters[inter] = params.get(inter)

    es_indexer = ESIndexerFactory.create_indexer(index_name=index_name)
    if not es_indexer:
        return return_value_400("indexer not exists")
    total_data, data = es_indexer.es_search(current_page=current_page, each_page=each_page,
                                            sort_by=sort_by, sort_direction=sort_direction,
                                            # query_string=value,
                                            filters=filters,
                                            query_setting=query_setting)

    page_data = get_page_data(total_data, each_page, current_page)
    re_data = []

    for item in data:
        re_data.append(item['_source'])

    page_data['data'] = re_data

    return page_data, 200


@rq.job(ttl=5)
def es_op_bulk(index_name: str, op: str, items, refresh=False):
    try:
        start_time = get_current_datetime()
        data = list()
        match op.upper():
            case ESOperationEnum.INDEX.name:
                op = ESOperationEnum.INDEX.value
                for item in items:
                    action = {"_op_type": op, "_index": index_name, "_id": item.get('id'), "_source": item}
                    # app.logger.info(item.get('id'))
                    data.append(action)
            case ESOperationEnum.UPDATE.name:
                op = ESOperationEnum.UPDATE.value
                for item in items:
                    action = {"_op_type": op, "_index": index_name, "_id": item.get('id'), "doc": item}
                    # app.logger.info(item.get('id'))
                    data.append(action)
            case _:
                app.logger.error('es bulk operation is not valid. check your bulk op value')
                return return_value_400("")

        resp = bulk(es, data, index=index_name, refresh=refresh, raise_on_error=True)
        if resp[0] == len(data):
            app.logger.info(
                f'🟢 Insert Success, data size : {len(data)} , spend time : {get_current_datetime() - start_time}')
            return return_value_201("")
        else:
            app.logger.error(f'🔴 Insert Failed, info:{resp}')
            return return_value_500("data insert es not success")
    except BaseException as e:
        app.logger.error(f'🔴 Exception: {e}')


@rq.job(result_ttl=5)
def es_index(item, index_name, refresh=False):
    try:
        es_indexer = ESIndexerFactory.create_indexer(index_name)
        es_indexer.es_index(item, refresh)
        app.logger.info(f'🟢 Single Insert Success.')
    except BaseException as e:
        app.logger.error(f'🔴 Single Insert Error:{e}')


@rq.job(result_ttl=5)
def es_update(item, index_name, refresh=False):
    try:
        es_indexer = ESIndexerFactory.create_indexer(index_name)
        es_indexer.es_update(item, refresh)
        app.logger.info(f'🟢 Single Update Success.')
    except BaseException as e:
        app.logger.error(f'🔴 Single Update Error:{e}')


@rq.job(result_ttl=5)
def es_delete(doc_id, index_name, refresh=False):
    try:
        es_indexer = ESIndexerFactory.create_indexer(index_name)
        es_indexer.es_delete(doc_id, refresh)
        app.logger.info(f'🟢 Single Delete Success.')
    except BaseException as e:
        app.logger.error(f'🔴 Single Delete Error:{e}')


def es_index_mapping(index_name):
    es_indexer = ESIndexerFactory.create_indexer(index_name)

    if not es_indexer:
        app.logger.error("[es_index] indexer not found - {}".format(index_name))
        return

    es_indexer.es_index_mapping()


# 获取页码数据
def get_page_data(total_data, each_page, current_page):
    x, y = divmod(total_data, each_page)

    if y == 0:
        total_page = x
    else:
        total_page = x + 1

    page_data = {
        'eachPage': each_page,
        'currentPage': current_page,
        'totalData': total_data,
        'totalPage': total_page
    }

    return page_data


def rebuild_es_mapping(index_name=None):
    if index_name:
        indexes = [index_name]
    else:
        indexes = app.config.get('ES_INDEX_PREFIX')
    for index in indexes:
        es_indexer = ESIndexerFactory.create_indexer(index_name=index)
        # es_indexer.create_es_index(number_of_shards=app.config.get('ES_DEFAULT_SHARDS'),number_of_replicas=app.config.get('ES_DEFAULT_REPLICAS'))
        es_indexer.create_es_index()


def validate_data(data):
    if isinstance(data, str):
        data = json.loads(data)
    items: dict
    items = data.get('data')
    if not items:
        return return_value_400("索引数据不能为空")
    df = pd.DataFrame(items)
    df['create_time'] = df.apply(lambda x: transfer_datetime(x.create_time), axis=1)
    df['update_time'] = df.apply(lambda x: transfer_datetime(x.update_time), axis=1)
    df['comment_time'] = df.apply(lambda x: transfer_datetime(x.comment_time), axis=1)
    df['star'].fillna(0, inplace=True)
    _data = df.to_dict(orient='records')
    return return_value_200("check success", data=_data)
