#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler
from _route import route


@route('/')
class index(BaseHandler):
    def get(self):
        self.render()

