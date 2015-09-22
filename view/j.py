#!/usr/bin/env python
#coding:utf-8

import json

from view._base import JsonHandler
from _route import route
from model.user import User
from model.qiniu_ import qiniu_token
from model.gid_ import gid


@route('/j/upload_token')
class upload_token(JsonHandler):
    def get(self):
        key = gid()
        self.finish(qiniu_token(key))


@route('/j/signin')
class _(JsonHandler):
    def post(self):
        o = self.json
        user = User.user_login(o.user_name, o.password)
        if user:
            self.set_secure_cookie("user", json.dumps(dict(user)))
        else:
            self.err.msg = '登录错误'

        self.finish(dict(err=self.err.to_dict()))


@route('/j/signup')
class _(JsonHandler):
    def post(self):
        o = self.json
        if not o.name:
            self.err.name = '请填写姓名'
        if not o.user_name:
            self.err.name = '请填写用户名'
        if not o.password:
            self.err.name = '请填写密码'

        if not self.err:
            User.user_new(o.name, o.user_name, o.password)

        self.finish(dict(err=self.err.to_dict()))
