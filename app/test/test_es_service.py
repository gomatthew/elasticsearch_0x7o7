"""
Test Cases for ES Service
"""
import json
import time
import unittest

from app.main.service.es_service import es_index_mapping, search_data, delete_data, rebuild_es_mapping, set_data
from app.test.base import BaseTestCase
from app.main.dto.v1.person_info_dto import PersonInfoDTO


class TestESService(BaseTestCase):
    """
    测试ES功能
    """
    # def test_es_temp(self):
    #     search_data({},index_name='duyun_standard_address_info',query_fields={},query_setting={})


    def test_es_index_mapping(self):
        # 查询未存在索引应报400
        es_index_mapping("not_exist_index")
        resp, status = search_data({}, index_name="not_exist_index", query_fields={}, query_setting={})
        self.assertEqual(status, 400)
        # 查询建立好索引应报200
        rebuild_es_mapping('unit_test_index')
        resp, status = search_data({}, index_name='unit_test_index', query_fields={}, query_setting={})
        self.assertEqual(status, 200)

    def test_es_service_single_mode(self):
        from app.main.util.dummy_data import gen_person
        person_data = gen_person()
        data = {'data': [person_data], 'index_name': 'unit_test_index', 'is_update': False}
        doc_id = person_data.get('id')
        # 单笔数据
        # 增
        resp, status = set_data(data, index_name='unit_test_index', refresh=True)
        self.assertEqual(201, status)
        # 查
        resp, status = search_data({'id': doc_id}, index_name='unit_test_index',
                                   query_fields=PersonInfoDTO.query_setting,
                                   query_setting={})
        self.assertEqual(200, status)
        searched_data = resp.get('data')[0]
        self.assertEqual(doc_id, searched_data.get('id'))
        # 改
        searched_data['person_name'] = '0x7o7'
        data = {'data': [searched_data], 'index_name': 'unit_test_index', 'is_update': True}
        resp, status = set_data(data, index_name='unit_test_index', refresh=True)
        self.assertEqual(201, status)
        resp, status = search_data({'id': doc_id}, index_name='unit_test_index',
                                   query_fields=PersonInfoDTO.query_setting,
                                   query_setting={})
        update_data = resp.get('data')[0]
        self.assertEqual('0x7o7', update_data.get('person_name'))
        # 删
        data = {'data': [doc_id]}
        resp, status = delete_data(data, index_name='unit_test_index', refresh=True)
        self.assertEqual(200, status)

        resp, status = search_data({'id': doc_id}, index_name='unit_test_index',
                                   query_fields=PersonInfoDTO.query_setting,
                                   query_setting={})
        self.assertEqual([], resp.get('data'))

    def test_es_service_multiple_mode(self):
        # 多笔数据
        # 增
        import faker
        from app.main.util.dummy_data import gen_person
        fake = faker.Faker('zh_CN')
        person_data_multiple = [gen_person() for i in range(10)]
        person_id_multiple = [i.get('id') for i in person_data_multiple]
        person_update_check = dict(zip(person_id_multiple, [fake.name() for i in range(10)]))
        data = {'data': person_data_multiple, 'index_name': 'unit_test_index', 'is_update': False}
        resp, status = set_data(data, index_name='unit_test_index', is_update=False, refresh=True)
        self.assertEqual(201, status)
        # 查
        resp, status = search_data({'id': json.dumps(person_id_multiple)}, index_name='unit_test_index',
                                   query_fields={'id': 'id'},
                                   query_setting=PersonInfoDTO.query_setting)
        self.assertEqual(200, status)
        self.assertEqual(10, len(resp.get('data')))

        searched_data = resp.get('data')
        # 改
        for update_person_name in searched_data:
            update_person_name['person_name'] = person_update_check.get(update_person_name.get('id'))
        data = {'data': searched_data, 'index_name': 'unit_test_index', 'is_update': False}
        resp, status = set_data(data, index_name='unit_test_index', is_update=True, refresh=True)
        self.assertEqual(201, status)

        resp, status = search_data({'id': json.dumps(person_id_multiple)}, index_name='unit_test_index',
                                   query_fields={'id': 'id'},
                                   query_setting=PersonInfoDTO.query_setting)
        update_data = resp.get('data')
        for person in update_data:
            self.assertEqual(person.get('person_name'), person_update_check.get(person.get('id')))
        # 删
        data = {'data': person_id_multiple}
        resp, status = delete_data(data, index_name='unit_test_index', refresh=True)
        self.assertEqual(200, status)
        resp, status = search_data({'id': json.dumps(person_id_multiple)}, index_name='unit_test_index',
                                   query_fields={'id': 'id'},
                                   query_setting=PersonInfoDTO.query_setting)

        self.assertEqual([], resp.get('data'))


if __name__ == '__main__':
    unittest.main()
