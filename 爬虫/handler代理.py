import urllib.request

http_handler=urllib.request.HTTPHandler(debuglevel=1)

opener=urllib.request.build_opener(http_handler)

urllib.request.install_opener(opener)

res=opener.open('http://www.baidu.com')

print(res.read().decode('utf8'))