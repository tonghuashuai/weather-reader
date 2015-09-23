#!/usr/bin/env python
#coding:utf-8

import sys
import re
import tornado.web
import mako.lookup
import mako.template
import json
import logging

from config import STATIC_HOST

from model.jsob import JsOb
from model.user import User

reload(sys)
sys.setdefaultencoding('utf8')



class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        super(BaseHandler, self).prepare()
        if self._is_ie_lt_8():
            self.template = '_ie8.html'
            self.render

    def _is_ie_lt_8(self):
        ret = False

        p = re.compile('.*?MSIE (\d+).0;.*?')
        m = re.findall(p, self.request.headers.get('User-Agent'))
        try:
            if m and int(m[0]) <= 8:
                ret = True

        except:
            pass
        
        return ret

    def initialize(self):
        template_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories=template_path,
                                                 input_encoding='utf-8',
                                                 output_encoding='utf-8')

    def render_string(self, filename, **kwargs):
        # kwargs["current_user"] = self.current_user
        # kwargs["WEB_INFO"] = self.web_info
        kwargs["STATIC_HOST"] = str(STATIC_HOST)
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return template.render(**namespace)

    # @property
    # def web_info(self):
    #     return WebInfo.web_info_get(True)

    def render(self, **kwargs):
        if not hasattr(self, 'template') or not self.template :
            module_name = self.__module__.replace('view.', '').replace('.', '/')
            filename = "{0}/{1}.html".format(module_name, self.__class__.__name__)
            self.template = "{0}{1}".format(filename[0].lower(), filename[1:])

        self.finish(self.render_string(self.template, **kwargs))

    # def get_current_user(self):
    #     user = None
    #     json_ = self.get_secure_cookie("user")
    #     if json_:
    #         user = User.from_json(json_)

    #     return user


class JsonHandler(BaseHandler):
    def prepare(self):
        args = self.request.arguments
        args = dict((k, v[0]) for k, v in args.iteritems())
        self.json = JsOb(args)
        self.err = JsOb()

        super(JsonHandler, self).prepare()
        
