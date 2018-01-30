import urllib.request



def savehtml(respond,filename):
    # 文件写入
    f=open(filename,'wb')
    f.write(respond)
    print('下载完成')
    f.close()

def lodpag(url,filename):
    reques=urllib.request.Request(url)
    reques.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71')
    respond=urllib.request.urlopen(url)

    savehtml(respond.read(),filename)


def respag(url,starpag,endpag):

    for pag in range(starpag,endpag):
        pn=(pag-1)*50
        tb_url=url+str(pn)
        filename='第'+str(pag)+'个.html'
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