# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Day(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    high_temp = Field() 
    low_temp = Field()
    high_humidity = Field()
    low_humidity = Field()
