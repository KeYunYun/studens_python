# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencetnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名
	positionname = scrapy.Field()
	positionlink = scrapy.Field()
	positionType = scrapy.Field()
	peopleNum = scrapy.Field()
	WorkLocation = scrapy.Field()
	publishTime = scrapy.Field()
