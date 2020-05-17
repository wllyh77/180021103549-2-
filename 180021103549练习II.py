sum=0
count=0
xstr=input("请输入一个数>>")
while xstr!="":
    a=eval(xstr)
    sum=sum+a
    count+=1
    xstr=input("请输入一个数>>")

print("\n平均值:",sum/count)
#180021103549 梁友辉
