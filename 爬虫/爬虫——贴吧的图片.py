import urllib.request
from lxml import etree
import os

def readPicture(newurl,filename):
    row=0
    reques = urllib.request.Request(newurl)
    #reques.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71')
    respond = urllib.request.urlopen(reques).read().decode('utf8')
    html=etree.HTML(respond)
    filelist=html.xpath('//img[@class="BDE_Image"]/@src')
    for fileurl in filelist:
        row=row+1
        filename=filename+"的第"+str(row)+"附图片.jpg"
        respond = urllib.request.urlopen(fileurl).read()
        savehtml(respond,filename)

def dealPicture(html,filename):
    low=0
    html = etree.HTML(html)
    result = html.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    for link in result:
        newurl='https://tieba.baidu.com'+link
        low=low+1
        filename=filename+'的第'+str(low)+'行'
        readPicture(newurl,filename)

def savehtml(respond,filename):
    # 文件写入

    f=open('./picture'+filename,'wb')
    f.write(respond)
    print('下载完成')
    f.close()

def lodpag(url,filename):
    reques=urllib.request.Request(url)
    #reques.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71')
    respond=urllib.request.urlopen(reques).read().decode('utf8')
    dealPicture(respond,filename)


def respag(url,starpag,endpag):

    for pag in range(starpag,endpag):
        pn=(pag-1)*50
        tb_url=url+str(pn)
        filename='第'+str(pag)+'个'
        lodpag(tb_url,filename)


def main():
    title = input('请输入要搜索的贴吧的名称')
    starepag = int(input('请输入搜索的其实页'))
    endpag = int(input('请输入搜索的末尾页'))
    wd = urllib.parse.urlencode({'kw': title})
    url = 'https://tieba.baidu.com/f?' + wd + '&pn='
    respag(url, starepag, endpag)


if __name__ == "__main__":
    main()