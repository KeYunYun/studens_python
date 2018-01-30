

f=open("C:/Users/kcy/Desktop/1.txt")
f2=open("123.txt","w+")
line=f.readline()
while line:
    f2.write(str(line[0:-1])+ " n\n")
    line=f.readline()

f.close()
f2.close()