from scrapy import Item, Field


class InstaligaItem(Item):
    user = Field()
    full_name = Field()
    bio = Field()
    num_posts = Field()
    num_followers = Field()
    num_following = Field()
