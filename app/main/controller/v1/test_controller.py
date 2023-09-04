"""
ES Service - Purchase Order
"""
from flask import request
from flask_restx import Resource
from app.main.dto.v1.test_dto import TestDTO
from app.main.service.es_service import index_data, search_data, delete_data

api = TestDTO.api
return_value = TestDTO.return_value


# 测试用例
@api.route('/v1')
@api.response(400, 'BAD REQUEST', model=return_value)
@api.response(401, 'NOT AUTHORIZED', model=return_value)
@api.response(500, 'SERVER ERROR', model=return_value)
class PurchaseOrderBatch(Resource):
    """
    Resource for Purchase Order Batch
    """

    @api.response(200, '获取成功', model=return_value)
    @api.doc(params=dict(TestDTO.query_conditions.items() | TestDTO.query_fields.items()))
    def get(self):
        """ 获取数据 """
        data = search_data(request.args, index_name='unit_test', query_fields=TestDTO.query_fields,
                           query_setting=TestDTO.query_setting)
        return data

    @api.response(201, '创建成功', model=return_value)
    @api.expect(TestDTO.test_data_input)
    def post(self):
        """ 创建数据 """
        resp, status = index_data(request.json, index_name="unit_test")
        return resp, status

    @api.response(200, '修改成功', model=return_value)
    @api.expect(TestDTO.test_data_input)
    def put(self):
        """ 修改数据 """
        resp, status = index_data(request.json, operation='update', index_name="unit_test")
        return resp, status

    @api.response(200, '修改成功', model=return_value)
    @api.expect(TestDTO.test_data_delete)
    def delete(self):
        """ 删除数据 """
        resp, status = delete_data(request.json, index_name="unit_test")
        return resp, status
