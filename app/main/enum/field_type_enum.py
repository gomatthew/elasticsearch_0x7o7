"""
搜索类型
"""
from enum import Enum


class FieldTypeEnum(Enum):
    """
    搜索类型
    """

    LIST = "列表"
    RANGE = "范围"
    DATETIME_RANGE = "时间范围"
    CONTAIN = "包含"

