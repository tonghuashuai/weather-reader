#!/usr/bin/env python
#coding:utf-8

import json
import tornado.websocket

from view._base import JsonHandler
from _route import route
from model.qiniu_ import qiniu_token

clients = list()

@route('/j/upload_token')
class upload_token(JsonHandler):
    def get(self):
        key = gid()
        self.finish(qiniu_token(key))


@route('/j/msg')
class MsgSocket(tornado.websocket.WebSocketHandler):
    # event when connecting
    def open(self):
        clients.append(self)

    # event when geting msg
    def on_message(self, msg):
        for client in clients:
            client.write_message(msg)

   # event when closing connecting
    def on_close(self):
        if self in clients:
            clients.remove(self)

