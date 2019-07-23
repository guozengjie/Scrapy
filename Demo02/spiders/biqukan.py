# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy import Request
from scrapy.selector import Selector

from Demo02.items import Demo02Item


class BiqukanSpider(scrapy.Spider):
    name = 'biqukan'
    allowed_domains = ['biqukan.com']
    start_urls = ['https://www.biqukan.com/3_3037/']

    def parse(self, response):
        # 创建一个选择器的实例
        select = Selector(response)
        dd_list = select.css("dd:nth-child(n+15)")
        for dd in dd_list:
            item = Demo02Item()
            item['title'] = dd.css('a::text').get()
            item['href'] = dd.css('a::attr(href)').get()
            request = Request(parse.urljoin(response.url, item['href']), callback=self.parse_body)
            yield request

    def parse_body(self, response):
        print('---------------------', response)
