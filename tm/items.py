# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OfficerItem(scrapy.Item):
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
    email = scrapy.Field()


class PathwayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    purpose = scrapy.Field()
    overview = scrapy.Field()
    includes1 = scrapy.Field()
    includes2 = scrapy.Field()
    includes3 = scrapy.Field()
    includes4 = scrapy.Field()
    includes5 = scrapy.Field()
    form1 = scrapy.Field()
    form2 = scrapy.Field()
    form3 = scrapy.Field()
