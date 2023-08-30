# -*- coding: utf-8 -*-
from enum import Enum


class ESOperationEnum(Enum):
    """
    bulk operation enum
    """
    INDEX = "index"
    UPDATE = "update"
    DELETE = "delete"
