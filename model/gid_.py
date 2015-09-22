#!/usr/bin/env python
#coding: utf-8

import _env
from db import redis

GLOBAL_ID = 'gid'

def gid():
    return redis.incr(GLOBAL_ID)

if __name__ == "__main__":
    pass
    print gid()

