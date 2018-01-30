def print_menu():
    print('调用函数')
    print('成功')




def print_rec():
    i=0
    while i<5 :
        j=1
       
        while j<=5:
            print('*'*j)
            j+=1
            i+=1

def addtwo(a,b):
    c=a+b
    print('%d'%c)

def returnadd(a,b):
    return a+b
    
a=100

def text1():
    a=200
    print('text1   %d'%a)
def text2():
    print('text2   %d'%a)
def text3():
    global a
    a=300
    print('text3   %d'%a)

def addmore(a,b,*args):
    reslut=a+b
    print(args)
    for temp in args:
        reslut+=temp
    return reslut
    

print_menu()
print_rec()
'''
num1=int(input('请输入第一个数字'))
num2=int(input('请输入第二个数字'))
addtwo(num1,num2)
print('结果为%d'%returnadd(num1,num2))
'''
text1()
text2()
text3()
text2()

print(addmore(1,2,3,4,5,6,7))
