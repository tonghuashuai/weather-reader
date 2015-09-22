#!/usr/bin/env python
#coding: utf-8

import time
import json

def time_fmt(timestamp, fmt='%Y-%m-%d %H:%M:%d'): 
    return time.strftime(fmt, time.localtime(timestamp))

def print_utf8(s):
    print json.dumps(s, encoding="UTF-8", ensure_ascii=False)

def extract(begin, end, html):
    if not html:
        return ''
    start = html.find(begin)
    if start >= 0:
        start += len(begin)
        if end is not None:
            end = html.find(end, start)
        if end is None or end >= 0:
            return html[start:end].strip()

def extract_all(begin, end, html):
    return map(str.strip, _extract_all(begin, end, html))

def _extract_all(begin, end, html):
    if not html:
        return ''
    result = []
    from_pos = 0
    while True:
        start = html.find(begin, from_pos)
        if start >= 0:
            start += len(begin)
            endpos = html.find(end, start)
            if endpos >= 0:
                result.append(html[start:endpos])
                from_pos = endpos+len(end)
                continue
        break
    return result
