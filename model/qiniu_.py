#!/usr/bin/env python
#coding: utf-8

import _env

import json
from qiniu import Auth
from config import QINIU

qiniu_ = Auth(QINIU.ACCESS_KEY, QINIU.SECRET_KEY)

# 上传策略仅指定空间名和上传后的文件名，其他参数仅为默认值
def qiniu_token(key):
    if key:
        key = str(key)
        policy = dict(
            scop="%s:%s" % (QINIU.BUCKET, key),
            returnBody="""{
                "key":$(key),
                "w": $(imageInfo.width),
                "h": $(imageInfo.height),
                "fn": $(fname)
            }""",
            saveKey=key)
        token = qiniu_.upload_token(QINIU.BUCKET, None, policy=policy )
        return token


if __name__ == "__main__":
    print qiniu_token(111)

