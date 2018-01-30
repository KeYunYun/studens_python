#encodeing=utf-8
from  MysqlHelper import *
from hashlib import sha1

name=input('请输入用户名：')
pwd=input('请输入密码')

#加密
sha=sha1()
sha.update(pwd.encode('utf-8'))
pwd2=sha.hexdigest
print(str(pwd2))

#根据用户名查询
query='select passwd from users where name=%s'
sqlhelper=MysqlHelper('localhost',3306,'pymysql','root','kcy000')
result=sqlhelper.all(query,[name])
if(len(result)==0):
    print('用户不存才')
elif result[0][0]==pwd2:
    print('登录成功')
else:
    print('密码错误')
print(result)