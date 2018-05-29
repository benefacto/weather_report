# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class pipeline(object):

    # appends item to existing CSV file
    def process_item(self, item, spider):
        output = open('output.csv', 'a')
        output.write(str(item))
        output.close()
        return item
