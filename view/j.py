#!/usr/bin/env python
#coding:utf-8

import json

from view._base import JsonHandler
from _route import route
# from model.user import User
from model.qiniu_ import qiniu_token
# from model.gid_ import gid


@route('/j/upload_token')
class upload_token(JsonHandler):
    def get(self):
        key = gid()
        self.finish(qiniu_token(key))

