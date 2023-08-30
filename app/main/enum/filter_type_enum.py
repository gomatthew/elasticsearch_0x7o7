"""
搜索设置
"""
from enum import Enum


class FilterTypeEnum(Enum):
    """
    搜索设置
    """

    SHOULD = "SHOULD"
    MUST = "MUST"
