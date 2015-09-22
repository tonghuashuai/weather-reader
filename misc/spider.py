#!/usr/bin/env python
# coding: utf-8
import _env  # noqa
import requests
import urllib
import time
from model.util import print_utf8, extract_all, extract
import logging


class Spider(object):
    '''爬虫基类.
    '''

    def __init__(
            self,
            host,
            search_url,
            iterable_url,
            max_page,
            time_wait=0,
            offset=0
    ):
        '''初始化.

        search_url和iterable_url应为有占位符的字符串.

        args:
            host, 域名,例如angelcrunch.com
            search_url, 搜索url,例如"/search?cat=company&keyword=%s"
            iterable_url, 网页格式,例如/resource/list/33720
        '''
        self.host = host
        self.search_url = search_url
        self.iterable_url = iterable_url
        self.max_page = max_page
        self.time_wait = time_wait
        self.offset = offset

    def __len__(self):
        return self.max_page

    def __iter__(self):
        for index in range(self.offset, self.max_page):
            time.sleep(self.time_wait)
            yield self.fetch(self.iterable_url % index, index)

    def resolve(self, html, page_id=0):
        raise NotImplemented("implement in subclass")

    def fetch(self, url, page_id=0):
        code = 0
        re_try = 0
        while code not in [200, 404] and re_try < 5:
            if re_try > 0:
                logging.warn("fail code=%s, retyring, %s" % (code, re_try))
            try:
                response = requests.get("http://%s%s" % (self.host, url))
                code = response.status_code
            except requests.exceptions.RequestException as e:
                logging.error(e)
            time.sleep(1)
            re_try += 1
        html = response.content

        return self.resolve(''.join(html.split()), page_id)

    def search(self, keyword):
        pass


class JuziSpider(Spider):

    def fetch_by_id(self, page_id):
        return self.fetch(self.iterable_url % page_id)

    def resolve(self, html, page_id):
        name = extract("<title>", "|IT桔子", html)
        html = extract("<body>", "</body>", html)
        base_info_html = extract(
            '<ulclass="detail-info">',
            "</ul>",
            html
        )

        # 提取基本信息
        domain = extract(
            'li>网址:<atarget="_blank"href="',
            '"',
            base_info_html
        )
        if domain:
            proto, rest = urllib.splittype(domain)
            res, rest = urllib.splithost(rest)
            if res.startswith("www."):
                res = res.split("www.")[1]
            domain = res
        location_html = extract("<li>地点", "</li>", base_info_html)
        location_list = filter(
            lambda item: not item == ',',
            extract_all('>', '<', location_html)
        )
        while len(location_list) < 2:
            location_list.append('')
        location1, location2 = location_list
        business_html = extract("li>行业", "</li>", base_info_html)
        business = extract(">", "<", business_html)
        sub_business_heml = extract("li>子行业", "</li>", base_info_html)
        sub_business = extract(">", "<", sub_business_heml)
        tag_html = extract("li>TAG", "</li>", base_info_html)
        tag_list = filter(
            lambda item: not item == ',',
            extract_all('>', '<', tag_html)
        )
        txt = extract("简介:<em>", "</em>", base_info_html)

        # 提取融资情况
        vc_list = []
        vc_html = extract('获投状态', '<divclass="normal-box">', html)
        vc_item_list = extract_all(
            '<divclass="company-fund-item">',
            '</div>',
            vc_html
        )
        for vc_item in vc_item_list:
            vc_round_html = extract("<h3>", "h3>", vc_item)
            vc_amount = extract(
                'ompany-fund-item-moneytext-center">',
                "</p>",
                vc_item
            )
            vc_id = extract("investevents/", "\"", vc_amount)
            if not vc_id:
                vc_id = extract("merger/", "\"", vc_amount)

            # <h3><bclass="pull-right">C轮</b>2014年6月</h3><pclass="company-fund-item-moneytext-center"><atarget="blank"href="http://itjuzi.com/investevents/3386">3000万美元</a></p><pclass="text-center"><ahref="http://itjuzi.com/investfirm/39">联创策源</a>　<ahref="http://itjuzi.com/investfirm/1">红杉资本中国</a>　<ahref="http://itjuzi.com/investfirm/27">贝塔斯曼亚洲投资基金/Betafund</a></p>
            vc_amount = extract(">", "</a>", vc_amount)
            vc_round = extract(">", "</", vc_round_html)
            vc_time = extract('b>', '<', vc_round_html)
            vc_name_html = extract_all("investfirm/", "a>", vc_item)
            vc_name_list = []
            for vc_name_item in vc_name_html:
                vc_name_list.append(
                    extract('>', '</', vc_name_item)
                )
            vc_list.append(dict(
                vc_id=vc_id,
                vc_round=vc_round,
                vc_time=vc_time,
                vc_amount=vc_amount,
                vc_name_list=vc_name_list
            ))

        return page_id, dict(
            # juzi_id=page_id,
            name=name,
            domain=domain,
            location1=location1,
            location2=location2,
            business=business,
            sub_business=sub_business,
            tag_list=tag_list,
            txt=txt,
            # vc_list=vc_list
        ), vc_list


def main():
    # from zapp.ANGELCRUNCH.model.itjuzi import Itjuzi, ItjuziVc
    sp = JuziSpider(
        'itjuzi.com',
        '/search?cat=company&keyword=%s',
        '/company/%s',
        23965,
        time_wait=0,
        offset=101,
    )
    print_utf8('hhh')
    # print_utf8(sp.fetch_by_id(300))
    for juzi_id, juzi_com, vc_list in sp:
        # logging.debug(juzi_id)
        juzi_id = int(juzi_id)
        if not juzi_com['name']:
            continue
        print_utf8(juzi_id)
        print_utf8(juzi_com)
        print_utf8(vc_list)
        # Itjuzi(juzi_com).upsert(dict(juzi_id=juzi_id))
        # for vc in vc_list:
        #     vc_id = int(vc.pop("vc_id"))
        #     ItjuziVc(vc).upsert(dict(juzi_id=juzi_id, vc_id=vc_id))

    # for item in sp:
    #     # pass
    #     print_utf8(item)
    pass

if __name__ == '__main__':
    main()
