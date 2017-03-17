# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from instaliga.items import InstaligaItem


class UserSpider(scrapy.Spider):
    name = "user"
    allowed_domains = ["instaliga.com"]
    users = pd.read_csv('../../data/users.csv')
    start_urls = ['http://www.instaliga.com/' + str(x) for x in users['users']]

    def parse(self, response):
        u = InstaligaItem()
        # assumes a list of 1
        import ipdb
        ipdb.set_trace()
        try:
            u['user'] = response.xpath(
                '//h1[@class="userMainInfo__name"]/text()').extract()[0].strip()
            u['full_name'] = response.xpath(
                '//div[@class="userMainInfo__bio"]/strong/text()').extract()[0].strip()
            u['bio'] = response.xpath(
                '//div[@class="userMainInfo__bio"]/text()').extract()[0].strip()
        except:
            pass
        # u['num_posts'] = response.xpath('//')
        # u['num_followers'] = response.xpath('//')
        # u['num_following'] = response.xpath('//')
        yield u
