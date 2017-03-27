# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from instaliga.items import InstaligaItem, TopPhotosItem
import datetime as dt
import re


class UserSpider(scrapy.Spider):
    name = "user"
    allowed_domains = ["instaliga.com"]
    users = pd.read_csv('../../data/users_Insta.csv')['user'].unique()
    start_urls = ['https://www.instaliga.com/' + str(x) for x in users]

    def parse(self, response):

        def get_social_info(key_xp, vals_xp):
            """
            Function to pull the posts, followers, following information and
            return a dict of key: value pairs
            """
            keys = response.xpath(key_xp).extract()
            keys = [x.replace(' ', '_') for x in keys if x != '']
            vals = response.xpath(vals_xp).extract()
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
                except Exception:
                    continue
            return item

        def clean_top_n_pics(item):

            def caption(item, k='caption'):
                # condensed = [x.strip() for x in item[k]]
                pass

            def likes(item, k='likes'):
                item[k] = [int(x) for x in item[k]]

            def comments(item, k='comments'):
                item[k] = [int(x.strip().replace(r'\xa', '')) for x in item[k]]

            def image(item, k='image'):
                item[k] = item[k]

            def hashtags(item, k='hashtags'):
                pat = re.compile(r'[#]\w+')
                clean = [x.replace('\n', ' ') for x in item[k]]
                item[k] = [x for x in map(
                    lambda x:
                        [y.replace('#', '') for y in pat.findall(x)], clean)]

            mapper = {
                'caption': caption(item),
                'likes': likes(item),
                'comments': comments(item),
                'image': image(item),
                'hashtags': hashtags(item)
            }

            for key in item.keys():
                mapper[key]

            return item

        u = InstaligaItem()
        p = TopPhotosItem()
        # assumes a list of 1
        # import ipdb; ipdb.set_trace()
        u['user'] = response.xpath(
            '//h1[@class="userMainInfo__name"]/text()').extract()
        u['full_name'] = response.xpath(
            '//div[@class="userMainInfo__bio"]/strong/text()').extract()
        u['bio'] = response.xpath(
            '//div[@class="userMainInfo__bio"]/text()').extract()
        u['scrape_time'] = dt.datetime.now()

        # automatically updates InstaligaItem object for social info
        social_info = get_social_info(
            key_xp='//div[@class="userInfo"]/text()',
            vals_xp='//div[@class="userInfo"]/div/text()'
        )

        u = update_fields(u, social_info)
        u = clean_results(u)

        p['image'] = response.xpath(
            '//ul[contains(@class, "mediaList")]/li/div/a/img/@src').extract()
        # p['caption'] = response.xpath(
        # '//li[@class = "element_comments__item"]/text()').extract()
        p['hashtags'] = response.xpath(
            '//a[@class = "element__image-wrapper"]/@title').extract()
        p['likes'] = response.xpath(
            '//span[@class = "likeCount"]/text()').extract()
        p['comments'] = response.xpath(
            '//div[@class = "activities actionBlock"]/text()').extract()

        u['top_N_photos'] = clean_top_n_pics(p)
        yield u
