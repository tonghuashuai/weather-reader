#!/usr/bin/env python
#coding:utf-8

from view._base import BaseHandler
from _route import route
from model import const

from model.news import News


@route('/')
class index(BaseHandler):
    def get(self):
        self.render()


@route('/reg')
class reg(BaseHandler):
    def get(self):
        self.render()


@route('/reg_success')
class reg_success(BaseHandler):
    def get(self):
        self.render()


@route('/about')
class about(BaseHandler):
    def get(self):
        self.render()

        
@route('/1nvestors')
class investors(BaseHandler):
    def get(self):
        self.render()


@route('/fund')
class fund(BaseHandler):
    def get(self):
        self.render()


@route('/news/(milestone|startup)')
class news(BaseHandler):
    def get(self, catagory):
        if catagory == 'startup':
            catagory = const.NEWS_CATAGORY.STARTUP
        else:
            catagory = const.NEWS_CATAGORY.NEWS

        spec = dict(catagory=catagory)
        title = const.NEWS_CATAGORY_CN.get(catagory)
        li = News.news(spec=spec)

        self.render(li=li, title=title)


@route('/contact')
class contact(BaseHandler):
    def get(self):
        self.render()
        

@route('/joinus')
class joinus(BaseHandler):
    def get(self):
        self.render()


@route('/signin')
class signin(BaseHandler):
    def get(self):
        self.render()


@route('/signup')
class signup(BaseHandler):
    def get(self):
        self.render()


@route('/signout')
class signup(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")
