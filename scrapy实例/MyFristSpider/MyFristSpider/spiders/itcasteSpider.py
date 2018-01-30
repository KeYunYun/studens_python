import scrapy
from MyFristSpider.items import MyfristspiderItem

class ItcastSpider(scrapy.Spider):
	#爬虫名
	name="itcast"
	#允许爬虫作用的范围
	allow_domains=["http://www.itcast.cn/"]
	#爬虫其实的URL
	start_urls=["http://www.itcast.cn/channel/teacher.shtml#"]
	
	
	
	def parse(self,response):
		item = MyfristspiderItem()
		teacherItem =[]
		teacher_list=response.xpath('//div[@class="li_txt"]')
		for each in teacher_list:
			name=each.xpath("./h3/text()").extract()[0]
			title=each.xpath("./h4/text()").extract()[0]
			info=each.xpath("./p/text()").extract()[0]
			
			item['name']=name
			item['title']=title
			item['info']=info
			
			yield item
			
		
		