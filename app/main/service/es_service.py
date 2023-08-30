import random
from traceback import format_exc
from app.main import rq, app
from app.main.lib.es_indexer_factory import ESIndexerFactory
from app.main.util.return_value import return_value_200, return_value_400, return_value_500
from app.main.enum.es_operation_enum import ESOperationEnum
from app.main.lib.datetimeLib import dt
from app.main.util.Util import redis_balance

def index_data(data, index_name, operation='index', refresh=False):
    """
    Create or update index data.
    """
    try:
        es_indexer = ESIndexerFactory.create_indexer(index_name)
        resp, status = validate_data(data)
        if status == 400:
            return resp, status
        if len(data) > 1:
            queue = redis_balance(app.config.get('BALANCE_KEY'))
            app.logger.info(f'🟢 bulk {operation} {es_indexer.index_name} - {len(data)} items with queue:{queue}.')
            es_indexer.es_op_bulk.queue(op=operation, items=data, refresh=refresh, queue=queue)
            # app.logger.info(f'🟢 {operation} done with code:{status}, spending time:{dt.datetime - start_time} seconds.')
            return return_value_200(message=f'{operation} accept')
        match operation.upper():
            case ESOperationEnum.INDEX.name:
                start_time = dt.datetime
                app.logger.info(f'🟢 {operation} {es_indexer.index_name} single data')
                resp, status = es_indexer.es_index(data, refresh=refresh)
                app.logger.info(f'🟢 {operation} done with code:{status},spending time:{dt.datetime - start_time} seconds.')
                return resp, status
            case ESOperationEnum.UPDATE.name:
                start_time = dt.datetime
                app.logger.info(f'🟢 {operation} {es_indexer.index_name} single data')
                resp, status = es_indexer.es_update(data, refresh=refresh)
                app.logger.info(f'🟢 {operation} done with code:{status},spending time:{dt.datetime - start_time} seconds.')
                return resp, status
    except BaseException as e:
        app.logger.error(format_exc())
        app.logger.error(e)
        return return_value_500("Server Error.")


def delete_data(data, index_name, refresh=False):
    es_indexer = ESIndexerFactory.create_indexer(index_name)
    resp, status = validate_data(data)
    if status == 400:
        return resp, status
    if len(data) > 1:
        resp, status = index_data(data, index_name, 'delete', refresh)
        return resp, status
    resp, status = es_indexer.es_delete(data)
    return resp, status

# def set_data(data, index_name, operation, is_update=False, refresh=False):
#     """
#     Create or update index data.
#     """
#     index_name = app.config.get('ES_INDEX_PREFIX') + index_name
#     resp, status = validate_data(data)
#     if status == 400:
#         return resp, status
#     # TODO do a batter balance
#     queue_num = str(random.randint(0, 9))
#     # queue_num = '0'
#     items = data.get('data')
#     if len(items) > 1:
#         match is_update:
#             case False:
#                 # if is_update is False:
#                 app.logger.info(f'bulk operation in queue:{queue_num}')
#                 set_data_bulk.queue(items, index_name, workers=queue_num, operation=operation, refresh=refresh,
#                                     queue=app.config.get("RQ_QUEUE_PREFIX") + queue_num)
#                 return return_value_201("index success")
#             case True:
#                 # elif is_update is True:
#                 app.logger.info(f'bulk operation in queue: update')
#                 set_data_bulk.queue(items, index_name, workers=queue_num, operation='update', refresh=refresh,
#                                     queue=app.config.get("RQ_QUEUE_PREFIX") + 'update')
#                 return return_value_201("update success")
#
#     # 单笔数据update&index
#     match is_update:
#         # for unit test
#         # es_update(items[0], index_name, refresh)
#         case True:
#             app.logger.info(f'single operation in queue:{queue_num}')
#             # es_update.queue(items, index_name, refresh, queue=app.config.get("RQ_QUEUE_PREFIX") + queue_num)
#             es_update(items, index_name, refresh)
#             return return_value_200("index success")
#         case False:
#             # for unit test
#             # es_index(items[0], index_name, refresh)
#             app.logger.info(f'single operation in queue: update')
#             es_index.queue(items, index_name, refresh, queue=app.config.get("RQ_QUEUE_PREFIX") + 'update')
#             return return_value_201("update success")



# def delete_data(data, index_name, refresh=False):
#     resp, status = validate_data(data)
#     if status == 400:
#         return resp, status
#     items = data.get('data')
#     if len(items) > 1:
#         set_data_bulk(items, index_name, operation='delete', refresh=refresh)
#         return return_value_200("delete success")
#     for item in items:
#         queue_name = app.config.get("RQ_QUEUE_PREFIX") + str(items.index(item) % len(app.config.get("QUEUES")))
#         # for unit test
#         # es_delete(item, index_name, refresh)
#         es_delete.queue(item, index_name, queue=queue_name)
#
#     return return_value_200("delete success")


# @rq.job(result_ttl=5)
# def set_data_bulk(items, index_name, workers, operation='index', refresh=False):
#     start_time = datetime.now()
#     batch = list()
#     for item in items:
#         action = {"_op_type": operation, "_index": index_name, "_source": item if operation != 'delete' else None,
#                   "_id": item.get('id') if operation != 'delete' else item}
#         batch.append(action)
#     bulk_operation_resp = bulk(es, batch, index=index_name, refresh=refresh)
#     end_time = datetime.now()
#     spend_time = (end_time - start_time).total_seconds()
#     success = 0
#     if bulk_operation_resp[0] == len(items):
#         app.logger.info(f'本次插入ES>{len(batch)}<笔数据,用时==>{spend_time}秒')
#     else:
#         app.logger.info(f'本次插入ES失败，ES反馈结果为:{bulk_operation_resp}')
#         success = 1
#     task_obj = TaskRecord()
#     task_obj.start_time = start_time
#     task_obj.spend_time = spend_time
#     task_obj.finish_time = end_time
#     task_obj.success = success
#     task_obj.data_rows = len(items)
#     task_obj.workers = workers
#     db.session.add(task_obj)
#     db.session.commit()


def search_data(params, index_name, query_fields, query_setting):
    each_page = int(params.get('eachPage', 10))
    current_page = int(params.get('currentPage', 1))
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

#
# @rq.job(result_ttl=5)
# def es_index(item, index_name, refresh=False):
#     es_indexer = ESIndexerFactory.create_indexer(index_name)
#     es_indexer.es_index(item, refresh)
#
#
# @rq.job(result_ttl=5)
# def es_update(item, index_name, refresh=False):
#     es_indexer = ESIndexerFactory.create_indexer(index_name)
#     es_indexer.es_update(item, refresh)
#
#
# @rq.job(result_ttl=5)
# def es_delete(doc_id, index_name, refresh=False):
#     es_indexer = ESIndexerFactory.create_indexer(index_name)
#     es_indexer.es_delete(doc_id, refresh)


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
        indexes = app.config.get('ES_INDEX')
    for index in indexes:
        es_indexer = ESIndexerFactory.create_indexer(index_name=index)
        # es_indexer.create_es_index(number_of_shards=app.config.get('ES_DEFAULT_SHARDS'),number_of_replicas=app.config.get('ES_DEFAULT_REPLICAS'))
        es_indexer.create_es_index()


def validate_data(data):
    items = data.get('data')
    if not items:
        return return_value_400("索引数据不能为空")
    return return_value_200("")
