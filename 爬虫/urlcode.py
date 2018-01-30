
import urllib.request

url ='http://www.baidu.com'
user_agent ='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'哈哈':'试试'}

data = urllib.parse.urlencode(values)
print(data)
req = urllib.request.Request(url)
req.add_header('User-Agent',user_agent)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))