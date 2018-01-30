#encoding=utf-8
import pymysql

try:
    #创建连接
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='kcy000',db='pymysql',charset='utf8')

    #创建游标
    cursor=conn.cursor()
    #执行sql语句
    resert=cursor.execute("insert into tb_info values(2,'李四','昭通','18468292851');")
    conn.commit()

    print(resert)

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

    # 执行SQL，并返回受影响行数,执行多次
    # effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])

    # 提交，不然无法保存新建或者修改的数据


    # 关闭游标
    cursor.close()
    # 关闭连接

    conn.close()

except Exception as e:
    print('连接出错%s'%e)
    pass