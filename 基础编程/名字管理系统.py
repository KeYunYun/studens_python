# 1. 打印功能提示
print("="*50)
print("     名字管理系统  ")
print("1.添加一个名字")
print("2.删除一个名字")
print("3.修改一个名字")
print("4.查询一个名字")
print("="*50)

# 2.获得用户输入
names=[]  #定义一个空的列表
isfig = True
while isfig:
    num=input("请输入你要选择的功能的序号")
    num=int(num)
    if num==1:
            new_name=input("请输入名字")
            names.append(new_name)
            print(names)

    elif num==2:
        dele_name=input("请输入要删除的名字")
        if dele_name in names:
            names.remove(dele_name)
            print(names)
        else:
            print("没有改名字")
    elif num==3:
        rename=input("请输入你要修改的名字")
        if rename in names:
           index= names.index(rename)
           revername=input("请输入你要改成什么名字")
           names[index]=revername;
           print(names)
        else:
            print("没有找到")
    elif num==4:
        check_name=input("请输入要查询的名字")
        if check_name in names :
            print("找到了")

        else:
            print("没有改名字")
    elif num==5:
        break
    else:
        print("输入有误")

    isfig_num = int(input("请输入是否继续操纵（1：是  2：否）"))
    if isfig_num == 1:
        isfig = True
    elif isfig_num == 2:
        isfig = False
    else:
        print("输入有误")


