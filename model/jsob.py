#!/usr/bin/env python
#coding: utf-8

class JsOb(object):
    def __init__(self, doc=dict()):
        if doc:
            for k, v in doc.iteritems():
                try:
                    v = int(v)
                except:
                    v = str(v)

                self.__dict__[k] = v

    def __getattr__(self, name):
        return self.__dict__.get(name, '')

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __repr__(self):
        return str(self.__dict__)

    def __len__(self):
        return self.__dict__.__len__()

    def to_dict(self):
        if self.__dict__:
            return self.__dict__
        else:
            return None

if __name__ == '__main__':
    jsob = JsOb()

    print jsob.to_dict()
