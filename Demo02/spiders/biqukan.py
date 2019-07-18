# -*- coding: utf-8 -*-
import scrapy


class BiqukanSpider(scrapy.Spider):
    name = 'biqukan'
    allowed_domains = ['biqukan.com']
    start_urls = ['https://www.biqukan.com/3_3037/']

    def parse(self, response):
        pass
