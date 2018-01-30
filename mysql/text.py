#encoding=utf-8

from  MysqlHelper import *

id1=input('请输入学号')
name =input('请输入名字')

sql='update tb_info set infoname=%s where id=%s'
params=[name,int(id1)]

sqlhelper=MysqlHelper('localhost',3306,'pymysql','root','kcy000')
sqlhelper.cud(sql,params)
query='select * from tb_info'
param=[]
print(sqlhelper.all(query,param))

