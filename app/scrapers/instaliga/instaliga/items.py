from scrapy import Item, Field


class InstaligaItem(Item):
    user = Field()
    full_name = Field()
    bio = Field()
    scrape_time = Field()
    top_N_photos = Field()


class TopPhotosItem(Item):
    image = Field()
    # caption = Field()
    hashtags = Field()
    likes = Field()
    comments = Field()
