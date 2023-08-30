from app.main.lib.es_indexer_base import ESIndexerBase


class ESIndexerPurchaseOrder(ESIndexerBase):
    """
    Purchase Order ES Indexer class
    """

    def __init__(self, name, task_id):
        super().__init__(name)
        self.task_id = task_id

    def get_es_mapping_fields(self):
        return {
            'transApplyCode': {"type": "keyword"},
            'revTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            'orderCreateTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            'otherContent': {"type": "keyword"},
            'content': {"type": "keyword"},
            'id': {"type": "long"},
            'serialNumber': {
                "type": "text",
                "analyzer": "char_analyzer",
                "search_analyzer": "char_analyzer",
            },
            'convertStatus': {"type": "keyword"},
            'sourceId': {"type": "long"},
            'fileIds': {"type": "keyword"},
            'sourceCode': {
                "type": "text",
                "analyzer": "char_analyzer",
                "search_analyzer": "char_analyzer",
            },
            'demandCode': {
                "type": "text",
                "analyzer": "char_analyzer",
                "search_analyzer": "char_analyzer",
            },
            'status': {"type": "keyword"},
            'orgCode': {"type": "keyword"},
            'orgName': {"type": "keyword"},
            'deptName': {"type": "keyword"},
            'deptCode': {"type": "keyword"},
            'providerCode': {"type": "keyword"},
            'providerName': {"type": "keyword"},
            'ownerCode': {"type": "keyword"},
            'ownerName': {"type": "keyword"},
            'contactUserName': {"type": "keyword"},
            'contactUserPhone': {"type": "keyword"},
            'devAddress': {"type": "keyword"},
            'revUserName': {"type": "keyword"},
            'revOrgCode': {"type": "keyword"},
            'revOrgName': {"type": "keyword"},
            'revUserPhone': {"type": "keyword"},
            'revAddress': {"type": "keyword"},
            'productStatus': {"type": "keyword"},
            'oneProductType': {"type": "keyword"},
            'twoProductType': {"type": "keyword"},
            'sourceType': {"type": "keyword"},
            'creditPeriod': {"type": "keyword"},
            'parityType': {"type": "keyword"},
            'frameworkContractNum': {"type": "keyword"},
            'deliveryTerms': {"type": "keyword"},
            'productMaterial': {"type": "keyword"},
            'amountWithTax': {"type": "keyword"},
            'amountWithoutTax': {"type": "keyword"},
            'sumPieceNum': {"type": "long"},
            'sumPurchaseNum': {"type": "double"},
            'sumOtherNum': {"type": "keyword"},
            'sumWeightNum': {"type": "keyword"},
            'sumAreaNum': {"type": "keyword"},
            'createUserName': {
                "type": "text",
                "analyzer": "char_analyzer",
                "search_analyzer": "char_analyzer",
            },
            'createUserId': {"type": "long"},
            'instockTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            'createTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            'closeTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
            'closeUserName': {"type": "keyword"},
            'closeUserId': {"type": "long"},
            'completeTime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"}

        }
