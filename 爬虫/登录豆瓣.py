#调用浏览器对象
from selenium import webdriver
#导入Keys 操作键盘，标签，鼠标
from selenium.webdriver.common.keys import Keys

#调用浏览器对象
driver=webdriver.PhantomJS()

driver.get("https://www.douban.com")