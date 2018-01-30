# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyfristspiderPipeline(object):
	#可选的，作为类的初始化
	def __init__(self):
		self.filename=open("teacher.json","w")
	#必须的，用于处理Item数据
    def process_item(self, item, spider):
		jsontext=json.dumps(dict(item),ensure_ascill=False)
        self.filename.write(jsontext.encode("utf-8"))
		return item
	#可选的，结束时调用
	def close_spider(self,spider):
		self.filename.close()
