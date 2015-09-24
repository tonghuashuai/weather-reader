#!/usr/bin/env python
#coding: utf-8

from enum import IntEnum

class IntEnum_(IntEnum):
    @classmethod
    def to_dict(cls):
        d = dict()
        for o in cls:
            d.update({o.name:o.value})

        return d


class OPS_CATAGORY(IntEnum_):
    MSG = 0
    OPS = 1

OPS_CATAGORY_CN = {
    OPS_CATAGORY.MSG: '消息',
    OPS_CATAGORY.OPS: '操作',
}


if __name__ == "__main__":
    pass
