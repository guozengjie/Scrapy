# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class BiqukanSpider(scrapy.Spider):
    name = 'biqukan'
    allowed_domains = ['biqukan.com']
    start_urls = ['https://www.biqukan.com/3_3037/']

    def parse(self, response):
        print(response)
        # 创建一个选择器的实例
        select = Selector(response)
        dd_list = select.css("dd:nth-child(n+15)")
        for dd in dd_list:
            pass
