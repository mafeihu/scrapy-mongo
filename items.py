# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # src = scrapy.Field()
    # img = scrapy.Field()
    num = scrapy.Field()
    play_date = scrapy.Field()
    pass