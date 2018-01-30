# coding: utf-8
import urllib.request
from lxml import etree
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71'}

def dealurl(url):
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request)
    htmlcode=respond.read()
    html = etree.HTML(htmlcode)

    return html


def gainbaidunews():
    pageNum=0
    url= "http://news.baidu.com/ns?word=title%3A%28"+urllib.request.quote("新工科专业")+"%29&pn="+str(pageNum)+"&cl=2&ct=1&tn=newstitle&rn=20&ie=utf-8&bt=0&et=0"
    print(url)
    html=dealurl(url)
    wedname=html.xpath('//div[@id="content_left"]/div[2]/div/div[@class="c-title-author"]/text()')
    wedload = html.xpath('//div[@id="content_left"]/div[2]/div/h3[@class="c-title"]/a/@href')

    for num in range(len(wedname)):
        print(wedname[num])
        if "高考网" in wedname[num]:
           savetext("来源于高考网\n")
           dealtosave(wedload[num],'//div[@class="content"]/div[@class="main"]/p/text()')
        if "网易" in wedname[num]:
            savetext("\n来源于网易\n")
            dealreguar(wedload[num],'<p style="color:#222222;font-family:arial, verdana, sans-serif;font-size:12px;"(.*?)</p>')
        if "阳光高考" in wedname[num]:
            savetext("\n来源于阳光高考\n")
            dealtosave(wedload[num],'/html/body/div[2]/div/div[2]/div[3]/div[1]/p/text()')
        if "中国教育在线" in wedname[num]:
            savetext("\n来源于中国教育在线\n")
            dealtosave(wedload[num], '//*[@id="mcontent"]/div[1]/p/text()')
        if "中国高校之窗" in wedname[num]:
            savetext("\n来源于中国高校之窗\n")
            dealtosave(wedload[num], '//div[@class="content"]/p/text()')
        if "新华网湖北站" in wedname[num]:
            savetext("\n来源于新华网湖北站\n")
            dealtosave(wedload[num], '//*[@id="nr_wz"]/p/text()')
        if "万家热线" in wedname[num]:
            savetext("\n来源于万家热线\n")
            dealtosave(wedload[num], '//div[@class="nt_cont_txt"]/div/p/text()')
        if "华禹教育网" in wedname[num]:
            savetext("\n来源于华禹教育网\n")
            dealreguar(wedload[num], '<td height="100%" span style="font-size:10.5pt;line-height: 18pt">(.*?)</td>')
        if "中国搜索" in wedname[num]:
            savetext("\n来源于中国搜索 \n")
            dealtosave(wedload[num], '//div[@class="detail-main"]/p/text()')
        if "中国日报" in wedname[num]:
            savetext("\n来源于中国日报 \n")
            dealtosave(wedload[num], '//*[@id="Contentp"]/text()')
        if "中国日报" in wedname[num]:
            savetext("\n来源于中国日报 \n")
            dealtosave(wedload[num], '//*[@id="Contentp"]/text()')
#

def dealtosave(url,xpath):
    html = dealurl(url)
    context = "\n".join(html.xpath(xpath))

    # print(context)
    savetext(context)

def dealreguar(url,regular):
    request = urllib.request.Request(url=url, headers=headers)
    respond = urllib.request.urlopen(request).read()
    #print(str(respond))
    pattern=re.compile(regular,re.DOTALL)
    content_list=pattern.findall(str(respond,'gbk'))
    savetext(" \n".join(content_list))


def savetext(context):
    file=open("news.txt","a+")
    file.write(context)
    file.closed

def gainzhihuweb():
    savetext("\n来源于知乎 \n")
    dealtosave("https://www.zhihu.com/question/58072589", '//div[@class="RichContent RichContent--unescapable"]/div/span/p/text()')

def main():
    gainbaidunews()
    
if __name__ == "__main__":
    main()
    gainzhihuweb()