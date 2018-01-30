import time

def sat_time():
    return time.ctime()


def appliction(env,start_response):
    '''必须有一个函数可以调用'''
    status='200 OK'
    headers=[
        ('Content-Type','text/plain')
    ]
    start_response(status,headers)
    return  sat_time()