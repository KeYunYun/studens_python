# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfristspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #姓名
	name=scrapy.Field()
	title=scrapy.Field()
	info=scrapy.Field()
