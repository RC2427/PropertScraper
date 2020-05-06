# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prop_title = scrapy.Field()
    prop_id = scrapy.Field()
    prop_price = scrapy.Field()
    prop_sqFeet = scrapy.Field()
    prop_link = scrapy.Field()
    prop_desc = scrapy.Field()
    prop_bhk = scrapy.Field()
    prop_img = scrapy.Field()
    pass
