def fun(c):
    max=c[0]
    for i in range(0,len(c)):
         if(max < a[i]):
              max = a[i]
    return max
def fun2(c):
    min=c[0]
    for i in range(0,len(c)):
         if(min > a[i]):
              min = a[i]
    return min
a=[]
b=eval(input("enter the limit"))
for i in range (0,b):
    item=input("enter the number")
    a.append(item)
f=fun(a)
g=fun2(a)
print(f,g)
