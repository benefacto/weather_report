# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Weather(Item):
    # define the fields for your item here like:
    # name = Field()
    day = Field()
    high_temp = Field() 
    low_temp = Field()
    high_humidity = Field()
    low_humidity = Field()
    
    # formats object as CSV string
    def __str__(self):
        return (self['day'] + "," + self['high_temp'] + "," + 
             self['low_temp'] + "," + self['high_humidity'] + "," +
             self['low_humidity'] + "\n")
