import urllib.request
from lxml import etree
import time
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71'}

def dealre(url):
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request).read()
    print(str(respond,'gbk'))
    re.DOTALL
    pattern=re.compile('<td height="100%" span style="font-size:10.5pt;line-height: 18pt">(.*?)</td>',re.DOTALL)
    content_list=pattern.findall(str(respond,'gbk'))
    print(content_list)
    print(" \n".join(content_list))

def dealurl(url):
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request).read()
    print(respond.decode())
    html = etree.HTML(respond)
    return html


def gainbaidunews():
    url = "https://www.zhihu.com/question/58072589"
    print(url)
    html = dealurl(url)
    wedname = html.xpath('//div[@class="RichContent RichContent--unescapable"]/div/span/p/text()')
    context = "\n".join(wedname)
    #
    print(context)
    # dealre(url)




def main():
    gainbaidunews()


if __name__ == "__main__":
    main()