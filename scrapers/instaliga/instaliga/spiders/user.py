# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from instaliga.items import InstaligaItem


class UserSpider(scrapy.Spider):
    name = "user"
    allowed_domains = ["instaliga.com"]
    users = pd.read_csv('../../data/users.csv')
    start_urls = ['https://www.instaliga.com/' +
                  str(x) for x in users['users']]

    def parse(self, response):

        def gxp(xpath):
            return response.xpath(xpath)

        def get_social_info(key_xp, vals_xp):
            """
            Function to pull the posts, followers, following information and
            return a dict of key: value pairs
            """
            keys = gxp(key_xp).extract()
            keys = [x.replace(' ', '_') for x in keys if x != '']
            vals = gxp(vals_xp).extract()
            return {keys: vals for keys, vals in list(zip(keys, vals))}

        def update_fields(obj, update, datatype='int'):
            for k in update.keys():
                obj.fields.update({k: {}})
                if datatype == 'int':
                    obj[k] = int(update[k])
                else:
                    obj[k] = update[k]
            return obj

        def clean_results(item):
            for k in item.keys():
                try:
                    if type(item[k]) is list:
                        item[k] = item[k][0].strip()
                    elif type(item[k]) is str:
                        item[k] = item[k].strip()
                except:
                    continue
            return item

        u = InstaligaItem()
        # assumes a list of 1
        # import ipdb; ipdb.set_trace()
        u['user'] = gxp(
            '//h1[@class="userMainInfo__name"]/text()').extract()
        u['full_name'] = gxp(
            '//div[@class="userMainInfo__bio"]/strong/text()').extract()
        u['bio'] = gxp(
            '//div[@class="userMainInfo__bio"]/text()').extract()

        # automatically updates InstaligaItem object for social info
        social_info = get_social_info(
            key_xp='//div[@class="userInfo"]/text()',
            vals_xp='//div[@class="userInfo"]/div/text()'
        )

        u = update_fields(u, social_info)
        u = clean_results(u)

        yield u
