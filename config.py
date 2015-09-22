#!/usr/bin/env python
#coding: utf-8

DEBUG = True

PORT = 8080

APP = '向日葵传媒'
APP_CN = 'Sunflower Media'
SLOGAN = '不辜负每一个梦想'

# HOST = 'http://xrkmedia.com'
# STATIC_HOST = 'http://static.xrkmedia.com'

HOST = 'http://c.cc:8088'
STATIC_HOST = 'http://static.c.cc:8088'

DB = 'sunflower'

MONGO_CONFIG = dict(
    host = "mongodb://127.0.0.1:27017",
)

REDIS_CONFIG = dict(
    host='127.0.0.1',
    port=6379,
    db=0
)

class QINIU(object):
    ACCESS_KEY = 'tZ1uxKB0hRo7bIOlHP0DkYDcNjFYAnW1LqzDsK_A'
    SECRET_KEY = 'v9G34Fy78Z5JRN26l7czcBJM1zNuG8CXgB5h491m'
    BUCKET = 'sunflower-website'
    HOST = 'http://7xk1xj.com1.z0.glb.clouddn.com'

