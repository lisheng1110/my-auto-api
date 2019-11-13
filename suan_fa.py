#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",j*i,end='\t')
    print()
#冒泡排序
a=[5,99,8,7,8,456,1,34]
length=len(a)
for i in range(length-1,0,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)