def addnum(num):
    if num>1:
        return num*addnum(num-1)
    else:
        return 1

print(addnum(4))
