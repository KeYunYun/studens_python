import pymysql
class MysqlHelper:
    def __init__(self,host,port,db,user,passwoed,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.password=passwoed
        self.charset=charset
    def connect(self):
        self.conn=pymysql.connect(host=self.host,
                                  port=self.port,db=self.db,user=self.user,
                                  password=self.password,charset=self.charset)
        self.cursor=self.conn.cursor()
        print('连接成功')
    def close(self):
        self.cursor.close()
        self.conn.close()


    def cud(self,sql,params):
        try:
            self.connect()
            print(sql)
            print(params)
            num=self.cursor.execute(sql,params)

            self.conn.commit()
            if num>0:
                print("修改成功")
            else:
                print('没有改变')

            self.close()
        except Exception as e:
            print(e)


    def all(self,sql,params):
        try:
            self.connect()
            self.cursor.execute(sql,params)
            result=self.cursor.fetchall()
            self.close()
            return result

        except Exception as e:
            print(e)
