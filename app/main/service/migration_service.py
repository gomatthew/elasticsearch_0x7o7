import random
import math
import requests
import json
import pandas as pd
from datetime import datetime
from app.main import app, db, rq
from app.main.service.es_service import index_data
from app.main.util.Util import http_post_request, camel_to_snake, AlchemyEncoder, DateEncoder
from app.main.model.tag_dict_model import TagDict
from app.main.util.dummy_data import gen_person
from concurrent.futures import ProcessPoolExecutor, wait, ALL_COMPLETED
from app.main.model.person_info_model import PersonInfo


def es_migrate_data(index_name, start_time, end_time, update_only=False):
    app.logger.info("*" * 10 + '开始导入es' + "*" * 10)
    migration_start_time = datetime.now()
    match index_name:
        case 'house_info':
            migrate_house_info(update_only, start_time, end_time)
        case 'person_info':
            migrate_person_info(update_only, start_time, end_time)
        case _:
            migrate_person_info_dummy()
    migration_end_time = datetime.now()
    app.logger.info("*" * 10 + '导入es结束' + "*" * 10)
    app.logger.info("总耗时==>%s" % str(migration_end_time - migration_start_time))


nation = TagDict.query.filter(TagDict.tag_code == 'nation').all()
gender = TagDict.query.filter(TagDict.tag_code == 'gender').all()
marriage = TagDict.query.filter(TagDict.tag_code == 'marital_status').all()
education_type = TagDict.query.filter(TagDict.tag_code == 'education_type').all()


def get_nation():
    nat = random.choice(nation)
    return nat.tag_code, nat.tag_name


def get_gender():
    gen = random.choice(gender)
    return gen.tag_code, gen.tag_name


def get_mariage_status():
    mar = random.choice(marriage)
    return mar.tag_code, mar.tag_name


def get_education_type():
    edu = random.choice(education_type)
    return edu.tag_code, edu.tag_name


def migrate_house_info(start_time, end_time, update_only):
    from app.main.model.house_info_view import HouseInfo
    app.logger.info("Start Migrating HouseInfo Index")
    per_page = 50000
    index = 0
    rq_prefix = app.config.get('RQ_QUEUE_PREFIX')
    filters = set()
    if start_time: filters.add(HouseInfo.create_time >= start_time)
    if end_time: filters.add(HouseInfo.create_time <= end_time)
    total_count = HouseInfo.query.filter(*filters).count()
    total_page = math.ceil(total_count / per_page) + 1
    migration_start_time = datetime.now()
    for page in range(1, total_page):
        app.logger.info("migration {}/{}".format(index, total_count))
        query_start_time = datetime.now()
        house_info_items = HouseInfo.query.filter(*filters).paginate(page, per_page,
                                                                     False).items
        # TODO query data
        data = house_info_items
        app.logger.info('本次查询数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        migrate_data('duyun_house_info', data, rq_prefix + str(page % 10))
        app.logger.info('本次处理数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        index = index + per_page
    migration_end_time = datetime.now()
    app.logger.info('需求主单导入es完成，耗时{}秒'.format(str(migration_end_time - migration_start_time)))
    app.logger.info("End Migrating HouseInfo Index")


def migrate_data(index_name, data, queue_name):
    app.logger.info(f'队列 {queue_name} 执行插入 {len(data)} 笔数据')
    set_data_bulk.queue(data, index_name, queue_name=queue_name)


def migrate_person_info(start_time, end_time, update_only):
    from app.main.model.person_info_view import PersonInfo
    app.logger.info("Start Migrating PersonInfo Index")
    per_page = 50000
    index = 0
    rq_prefix = app.config.get('RQ_QUEUE_PREFIX')
    filters = set()
    if start_time: filters.add(PersonInfo.create_time >= start_time)
    if end_time: filters.add(PersonInfo.create_time <= end_time)
    total_count = PersonInfo.query.filter(*filters).count()
    total_page = math.ceil(total_count / per_page) + 1
    migration_start_time = datetime.now()
    for page in range(1, total_page):
        app.logger.info("migration {}/{}".format(index, total_count))
        query_start_time = datetime.now()
        house_info_items = PersonInfo.query.filter(*filters).paginate(page, per_page,
                                                                      False).items
        # TODO query data
        data = house_info_items
        app.logger.info('本次查询数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        migrate_data('duyun_person_info', data, rq_prefix + str(page % 10))
        app.logger.info('本次处理数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        index = index + per_page
    migration_end_time = datetime.now()
    app.logger.info('需求主单导入es完成，耗时{}秒'.format(str(migration_end_time - migration_start_time)))
    app.logger.info("End Migrating PersonInfo Index")


def migrate_company_info(start_time, end_time, update_only):
    from app.main.model.company_info_view import CompanyInfo
    app.logger.info("Start Migrating CompanyInfo Index")
    per_page = 50000
    index = 0
    rq_prefix = app.config.get('RQ_QUEUE_PREFIX')
    filters = set()
    if start_time: filters.add(CompanyInfo.create_time >= start_time)
    if end_time: filters.add(CompanyInfo.create_time <= end_time)
    total_count = CompanyInfo.query.filter(*filters).count()
    total_page = math.ceil(total_count / per_page) + 1
    migration_start_time = datetime.now()
    for page in range(1, total_page):
        app.logger.info("migration {}/{}".format(index, total_count))
        query_start_time = datetime.now()
        house_info_items = CompanyInfo.query.filter(*filters).paginate(page, per_page,
                                                                       False).items
        # TODO query data
        data = house_info_items
        app.logger.info('本次查询数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        migrate_data('duyun_person_info', data, rq_prefix + str(page % 10))
        app.logger.info('本次处理数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        index = index + per_page
    migration_end_time = datetime.now()
    app.logger.info('需求主单导入es完成，耗时{}秒'.format(str(migration_end_time - migration_start_time)))
    app.logger.info("End Migrating CompanyInfo Index")


def migrate_acode_fence_info(start_time, end_time, update_only):
    from app.main.model.adcode_fence_info_model import AdcodeFenceInfo
    app.logger.info("Start Migrating AcodeFenceInfo Index")
    per_page = 50000
    index = 0
    rq_prefix = app.config.get('RQ_QUEUE_PREFIX')
    filters = set()
    if start_time: filters.add(AdcodeFenceInfo.create_time >= start_time)
    if end_time: filters.add(AdcodeFenceInfo.create_time <= end_time)
    total_count = AdcodeFenceInfo.query.filter(*filters).count()
    total_page = math.ceil(total_count / per_page) + 1
    migration_start_time = datetime.now()
    for page in range(1, total_page):
        app.logger.info("migration {}/{}".format(index, total_count))
        query_start_time = datetime.now()
        house_info_items = AdcodeFenceInfo.query.filter(*filters).paginate(page, per_page,
                                                                           False).items
        # TODO query data
        data = house_info_items
        app.logger.info('本次查询数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        migrate_data('duyun_person_info', data, rq_prefix + str(page % 10))
        app.logger.info('本次处理数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        index = index + per_page
    migration_end_time = datetime.now()
    app.logger.info('需求主单导入es完成，耗时{}秒'.format(str(migration_end_time - migration_start_time)))
    app.logger.info("End Migrating AdcodeFenceInfo Index")


def migrate_standard_address_info(start_time, end_time, update_only):
    from app.main.model.standard_address_info_view import StandardAddress
    app.logger.info("Start Migrating StandardAddress Index")
    per_page = 50000
    index = 0
    rq_prefix = app.config.get('RQ_QUEUE_PREFIX')
    filters = set()
    if start_time: filters.add(StandardAddress.create_time >= start_time)
    if end_time: filters.add(StandardAddress.create_time <= end_time)
    total_count = StandardAddress.query.filter(*filters).count()
    total_page = math.ceil(total_count / per_page) + 1
    migration_start_time = datetime.now()
    for page in range(1, total_page):
        app.logger.info("migration {}/{}".format(index, total_count))
        query_start_time = datetime.now()
        house_info_items = StandardAddress.query.filter(*filters).paginate(page, per_page,
                                                                           False).items
        # TODO query data
        data = house_info_items
        app.logger.info('本次查询数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        migrate_data('duyun_person_info', data, rq_prefix + str(page % 10))
        app.logger.info('本次处理数据{}笔，耗时{}秒'.format(len(data), str(datetime.now() - query_start_time)))
        index = index + per_page
    migration_end_time = datetime.now()
    app.logger.info('需求主单导入es完成，耗时{}秒'.format(str(migration_end_time - migration_start_time)))
    app.logger.info("End Migrating StandardAddress Index")


def migrate_person_info_dummy():
    # app.logger.info('开始导入')
    start_time = datetime.now()
    count = 0
    workers = app.config.get('PROCESS_WORKERS')
    executor = ProcessPoolExecutor(max_workers=workers)
    # all_task = [executor.submit(task, i) for i in range(1, 10000)]
    _tasks = app.config.get('TASKS')
    for q in range(1, _tasks + 1):
        q_ = q % 6
        app.logger.info(f"push job in queue:{q_}")
        task_.queue(i=q_, queue=f"queue_{q_}")
    end_time = datetime.now()
    app.logger.info(
        f'End Migrating PersonInfo Index; spend total time:{str(end_time - start_time)},total count:{count}')
    return
    all_task = [executor.submit(task_, i) for i in range(1, _tasks + 1)]
    wait(all_task, return_when=ALL_COMPLETED)
    end_time = datetime.now()
    app.logger.info(
        f'End Migrating PersonInfo Index; spend total time:{str(end_time - start_time)},total count:{count}')


@rq.job(result_ttl=5)
def task_(i):
    app.logger.info(f"添加5000笔数据")
    s_t = datetime.now()
    df = pd.DataFrame([gen_person() for i_ in range(4000)])
    df.to_sql(name="person_info", con=db.engine, index=False, if_exists="append")
    e_t = datetime.now()
    app.logger.info(f"添加5000笔数据 耗时:{str(e_t - s_t)}")


def task(i):
    a = i
    s_t = datetime.now()
    batch = list()
    # for i_ in range((i % 10 + 1) * 500):

    for i_ in range(2000):
        # count += 5000
        batch.append(gen_person())
    data = json.dumps({'data': batch}, cls=DateEncoder)

    resp = requests.post(url='http://127.0.0.1:8000/v1/person_info/batch', data=data,
                         headers={'Content-Type': 'application/json'})
    e_t = datetime.now()
    app.logger.info(f'{resp},耗时{str(e_t - s_t)}')
