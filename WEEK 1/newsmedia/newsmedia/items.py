# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostList(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link_url = scrapy.Field()
    time = scrapy.Field()
    categories = scrapy.Field()
    pass
