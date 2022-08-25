# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field()
    img = scrapy.Field()
    position_c = scrapy.Field()
    position_e = scrapy.Field()
    cname = scrapy.Field()
    ename = scrapy.Field()
    title = scrapy.Field()
    telephone = scrapy.Field()
