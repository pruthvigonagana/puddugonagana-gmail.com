def fun(a):
 b=a
 c=a
 sum=0
 count=0
 while a>0:
    a=a//10
    count=count+1
 while b>0:
        e=b%10
        sum+=e**count
        b=b//10
        if (sum==c):
          print(sum)
for i in range(1,155):
    fun(i)
