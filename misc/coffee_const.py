#!/usr/bin/env python
#coding: utf-8


from mako.template import Template
from mako.lookup import TemplateLookup
import _env


lookup = TemplateLookup(directories=['coffee'], output_encoding='utf-8')

template = lookup.get_template("const.coffee.mako")

with open('coffee/const.coffee', 'w+') as f:
    f.write(template.render())

