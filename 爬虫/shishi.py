from lxml import etree

text = etree.parse('./第2个.html', etree.HTMLParser())

#html = etree.HTML(text)
result = etree.tostring(text)

result = text.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
print(result)
