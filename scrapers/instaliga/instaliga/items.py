from scrapy import Item, Field


class InstaligaItem(Item):
    user = Field()
    full_name = Field()
    bio = Field()
    scrape_time = Field()
