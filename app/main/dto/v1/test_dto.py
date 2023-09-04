from flask_restx import Namespace, fields

from app.main.dto import get_parser, return_value_dto
from app.main.enum.field_type_enum import FieldTypeEnum
from app.main.enum.filter_type_enum import FilterTypeEnum


class TestDTO(object):
    """ 测试用dto """
    api = Namespace('测试api', description='test only')
    parser = get_parser(api)
    return_value = return_value_dto(api)

    test_model = api.model('Test Only', {
        "id": fields.String(required=True, description='数据id'),
        "comment_detail": fields.String(description='评论详情'),
        "comment_person": fields.String(description='评论人'),
        "comment_time": fields.DateTime(description='评论时间'),
        "hosp_id": fields.String(required=True, description='门店id'),
        "star": fields.Integer(description='评分'),
        "create_time": fields.DateTime(description='记录创建时间'),
        "update_time": fields.DateTime(description='记录更新时间'),
        "url": fields.String(required=True, description='网址'),
        "vip_tag": fields.Integer(description='vip标签')}
                           )
    test_data_input = api.model("test_model_input", {
        # 'callbackUrl': fields.String(required=True, description='回调URL'),
        'data': fields.List(fields.Nested(test_model, required=True, description='测试数据'))
    })

    test_data_output = api.model('测试数据查询结果', {
        'eachPage': fields.Integer(required=True, description='每页条数'),
        'currentPage': fields.Integer(required=True, description='当前页码'),
        'totalData': fields.Integer(required=True, description='数据总量'),
        'totalPage': fields.Integer(required=True, description='页数总量'),
        'data': fields.List(fields.Nested(test_model, required=True, description='测试数据列表'))
    })

    test_data_delete = api.model('test_data_delete', {
        'ids': fields.List(fields.String(required=True, description='id'))

        # 'purchase_order_ids': fields.List(cls_or_instance="['id']")
    })

    query_conditions = {
        'eachPage': '每页条数',
        'currentPage': '当前页数',
        'sortBy': '排序字段',
        'sortDirection': '升序：asc，降序：desc'
    }

    query_fields = {
        "id": "记录id",
        "comment_detail": "评论详情",
        "comment_person": "评论人",
        "comment_time": "评论时间 , ['datetime','datetime']",
        "hosp_id": '门店id',
        "star": '评分',
        "create_time": "记录创建时间 ['datetime','datetime']",
        "update_time": "记录更新时间 ['datetime','datetime']",
        "url": '网址',
        "vip_tag": 'vip标签'}

    query_setting = {
        "id": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.LIST.name
        },
        "comment_detail": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.CONTAIN.name
        },
        "comment_person": {
            "filter_type": FilterTypeEnum.MUST.name,
            # "field_type": FieldTypeEnum.LIST.name
        },
        "comment_time": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.DATETIME_RANGE.name
        },
        "hosp_id": {
            "filter_type": FilterTypeEnum.MUST.name,
            # "field_type": FieldTypeEnum.LIST.name
        },
        "star": {
            "filter_type": FilterTypeEnum.MUST.name,
            # "field_type": FieldTypeEnum.LIST.name
        },
        "create_time": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.DATETIME_RANGE.name
        },
        "update_time": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.DATETIME_RANGE.name
        },
        "url": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.CONTAIN.name
        },
        "vip_tag": {
            "filter_type": FilterTypeEnum.MUST.name,
            # "field_type": FieldTypeEnum.LIST.name
        }

    }
