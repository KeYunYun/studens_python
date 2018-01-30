# -*- coding: utf-8 -*-
import scrapy
from tencetn.items import TencetnItem
#导入CrawlSpider类和rule
from scrapy.spider import  CrawlSpider ,Rule
from scrapy.linkextractors import LinkExtractor

class TencentpositionSpider(CrawlSpider):
	name = "tencentPosition"
	allowed_domains = ["tencent.com"]
	start_urls = ["http://hr.tencent.com/position.php?&start=10#a"]

	pageLink=LinkExtractor(allow=("start=\d+"))

	rules = [
		Rule(pageLink,callback="parseTencent",follow=True)
	]
	#批量处理url

	def parseTencent(self,response):
		for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
			item = TencetnItem()
			item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
			item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
			item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
			item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]
			item['WorkLocation'] = each.xpath('./td[4]/text()').extract()[0]
			item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
			yield item  # 交个管道处理
