import urllib.request

httpproxy_handler=urllib.request.ProxyHandler({'http':'119.90.63.3'})

opener=urllib.request.build_opener(httpproxy_handler)

urllib.request.install_opener(opener)
respond=opener.open("http://www.baidu.com/")

print(respond.read().decode())