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

# @route('/j/msg')
# class msg(JsonHandler):
#     def post(self):
#         self.finish()

@route('/j/msg')
class MsgSocket(tornado.websocket.WebSocketHandler):
    #连接websocket服务器时进行的event
    def open(self):
        clients.append(self)

    #收到信息的时候进行的动作
    def on_message(self, message):
        #write_message用于主动写信息，这里将收到的信息原样返回
        print u"You said: " + message
        for client in clients:
            client.write_message(u"You said: " + message)

   #关系连接时的动作
    def on_close(self):
        if self in clients:
            clients.remove(self)

