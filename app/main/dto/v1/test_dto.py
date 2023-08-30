from flask_restx import Namespace, fields

from app.main.dto import get_parser, return_value_dto
from app.main.enum.field_type_enum import FieldTypeEnum
from app.main.enum.filter_type_enum import FilterTypeEnum


class TestDTO(object):
    """ 测试用dto """
    api = Namespace('测试api', description='test only')
    parser = get_parser(api)
    return_value = return_value_dto(api)

    purchase_order = api.model('Purchase Order', {
        'transApplyCode': fields.String(required=True, description='调拨申请单号'),
        'revTime': fields.DateTime(required=True, description='预计收货时间'),
        'orderCreateTime': fields.DateTime(required=True, description='订单创建时间'),
        'otherContent': fields.String(required=False, description='其它备注'),
        'content': fields.String(required=False, description='备注'),
        'id': fields.Integer(required=True, description='主键id'),
        'serialNumber': fields.String(required=False, description='单据号'),
        'convertStatus': fields.String(required=False, description='下游单据状态'),
        'sourceId': fields.Integer(required=False, description='来源id'),
        'sourceCode': fields.String(required=False, description='来源单号'),
        'demandCode': fields.String(required=False, description='需求单号'),
        'status': fields.String(required=False, description='订单状态'),
        'orgCode': fields.String(required=False, description='采购组织编码'),
        'orgName': fields.String(required=False, description='采购组织名称 '),
        'deptName': fields.String(required=False, description='部门名称'),
        'deptCode': fields.String(required=False, description='部门编码'),
        'providerCode': fields.String(required=False, description='供应商编码'),
        'providerName': fields.String(required=False, description='供应商名称'),
        'ownerCode': fields.String(required=False, description='货主编码'),
        'ownerName': fields.String(required=False, description='货主名称'),
        'contactUserName': fields.String(required=False, description='联系人'),
        'contactUserPhone': fields.String(required=False, description='联系电话'),
        'devAddress': fields.String(required=False, description='发货地址'),
        'revUserName': fields.String(required=False, description='收货人'),
        'revOrgCode': fields.String(required=False, description='收货人组织编码'),
        'revOrgName': fields.String(required=False, description='收货人组织名称'),
        'revUserPhone': fields.String(required=False, description='收货人电话'),
        'revAddress': fields.String(required=False, description='收货地址'),
        'productStatus': fields.String(required=False, description='物资状态'),
        'oneProductType': fields.List(fields.String, required=True, description='一级物料分类'),
        'twoProductType': fields.List(fields.String, required=False, description='二级物料分类'),
        'sourceType': fields.String(required=False, description='来源类型'),
        'creditPeriod': fields.String(required=False, description='账期'),
        'parityType': fields.String(required=False, description='比价方式'),
        'frameworkContractNum': fields.String(required=False, description='框架合同号'),
        'deliveryTerms': fields.String(required=False, description='交货条款'),
        'productMaterial': fields.List(fields.String, required=False, description='物资材质'),
        'amountWithTax': fields.String(required=False, description='含税金额'),
        'amountWithoutTax': fields.String(required=False, description='未税金额'),
        'sumPieceNum': fields.Integer(required=False, description='计件总数'),
        'sumPurchaseNum': fields.String(required=False, description='采购单位总数'),
        'sumOtherNum': fields.String(required=False, description='其他单位总数'),
        'sumWeightNum': fields.String(required=False, description='计重总数'),
        'sumAreaNum': fields.String(required=False, description='面积总数'),
        'createUserName': fields.String(required=False, description='创建人'),
        'createUserId': fields.Integer(required=True, description='创建人'),
        'instockTime': fields.DateTime(required=False, description='入库时间'),
        'createTime': fields.DateTime(required=False, description='账创建时间'),
        'closeTime': fields.DateTime(required=False, description='关闭时间'),
        'closeUserName': fields.String(required=False, description='关闭人'),
        'closeUserId': fields.Integer(required=False, description='关闭人id'),
        'completeTime': fields.DateTime(required=False, description='完成时间'),
        'fileIds': fields.String(required=False, description='附件id数组串'),

    })
    purchase_order_input = api.model("Purchase_Order_Input", {
        'callbackUrl': fields.String(required=True, description='回调URL'),
        'data': fields.List(fields.Nested(purchase_order, required=True, description='采购订单'))
    })

    purchase_order_output = api.model('采购订单查询结果', {
        'eachPage': fields.Integer(required=True, description='每页条数'),
        'currentPage': fields.Integer(required=True, description='当前页码'),
        'totalData': fields.Integer(required=True, description='数据总量'),
        'totalPage': fields.Integer(required=True, description='页数总量'),
        'data': fields.List(fields.Nested(purchase_order, required=True, description='采购订单列表'))
    })

    purchase_order_delete = api.model('Purchase_Delete', {
        'purchase_order_ids': fields.String(required=True,description='订单id')
        # 'purchase_order_ids': fields.List(cls_or_instance="['id']")
    })

    query_conditions = {
        "value": '搜索数据值',
        'eachPage': '每页条数',
        'currentPage': '当前页数',
        'sortBy': '排序字段',
        'sortDirection': '升序：asc，降序：desc'
    }

    query_fields = {
        "id": "记录id",
        "createUserName": "创建人",
        "serialNumber": "订单号",
        "orgCode": "采购组织编码, ['xx','xxx']",
        "orgName": "采购组织名称",
        "providerCode": "供应商编码, ['xx','xxx']",
        "demandCode": "需求单号",
        "sourceCode": "来源单号",
        "oneProductType": '一级物料分类, ["xx", "xxx"]',
        "twoProductType": '二级物料分类, ["xx", "xxx"]',
        "status": '单据状态, ["xx", "xxx"]',
        "createUserId": "创建人id",
        "checkTime": "审核时间,['start', 'end']",
        "closeTime": "关闭时间,['start', 'end']",
        "createTime": "创建时间, ['start', 'end']",
        "orderCreateTime": "订单创建时间,['start', 'end']",
        "closerId": "关闭人",
        "deptCode": "部门编码, ['xx','xxx']"
    }

    query_setting = {
        "id": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "serialNumber": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.CONTAIN.name
        },
        "createUserName": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.CONTAIN.name
        },
        "providerCode": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "orgCode": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "demandCode": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.CONTAIN.name
        },
        "sourceCode": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.CONTAIN.name
        },
        "productMaterial": {
            "filter_type": FilterTypeEnum.MUST.name,
            "field_type": FieldTypeEnum.LIST.name
        },
        "oneProductType": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "twoProductType": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "deptCode": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "status": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.LIST.name
        },
        "createTime": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.RANGE.name
        },
        "checkTime": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.RANGE.name
        },
        "closeTime": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.RANGE.name
        },
        "orderCreateTime": {
            "filter_type": FilterTypeEnum.MUST.name,
            "filed_type": FieldTypeEnum.RANGE.name
        }
    }
