import re
import urllib.request

re.compile('<div\sclass="desc">(.*?)<\div>')

class Spider:
    def __init__(self):
        pass
    def loadPage(self,page):
        url='http://www.neihan8.com/article/index_'+str(page)+'.html'
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71'}
        request=urllib.request.Request(url=url,headers=headers)
        respond=urllib.request.urlopen(request)

        html=respond.read();
        pattern=re.compile('<div class="desc"> (.*?)</div>')
        content_list=pattern.findall(html.decode("utf8"))
        for content in content_list:
            print(content)


    def writePage(self):
        pass
    def dealPage(self):
        pass
    def startWork(self):
        '''控制'''
        pass
def main():
    spain= Spider()
    spain.loadPage(2)

if __name__=='__main__':
    main()