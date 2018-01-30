import requests
from bs4 import BeautifulSoup
import urllib.request
import time

def captcha(captchadata):
    with open('captcha.jpg','wb')as f:
        f.writable(captchadata)
    text=input("请输入验证码")
    return text
def loadZhuhu():
    url="https://www.zhihu.com/#signin"
    heards={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.71'}
    request=urllib.request.Request(url,headers=heards)
    respond=urllib.request.urlopen(request).read().decode('utf8')
    # 调用lxml解析库
    bs = BeautifulSoup(respond, "lxml")

    # _xsrf 作用是防止CSRF攻击（跨站请求伪造)，通常叫跨域攻击，是一种利用网站对用户的一种信任机制来做坏事
    # 跨域攻击通常通过伪装成网站信任的用户的请求(利用Cookie)，盗取用户信息、欺骗web服务器
    # 所以网站会通过设置一个隐藏字段来存放这个MD5字符串，这个字符串用来校验用户Cookie和服务器Session的一种方式

    # 找到name属性值为 _xsrf 的input标签，再取出value 的值
    _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
    print(_xsrf)

    pictureurl='https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000)
    captchdate=urllib.request.urlopen(pictureurl).read()
    text=captcha(captchdate)

    #构建数据
    data={
        "_xsrf":_xsrf,
        "phone_num":'18468299501',
        "password":'kcy000',
        "captcha":text,
        "captcha_type":"cn"
    }

    post=urllib.request.Request("https://www.zhihu.com/login/phone_num ",data=data,headers=heards)
    postrepsond=urllib.request.urlopen(post)


def loadrequests():
    r = requests.get("https://www.zhihu.com/#signin")
    print(r.text)


def main():
    loadZhuhu()
if __name__=="__main__":
    main()
