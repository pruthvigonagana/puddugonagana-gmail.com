a=eval(input("enter the number"))
sum=0
rev=0
count=0
while a>0:
    d=a%10
    sum+=d
    rev=rev*10+d
    a=a//10
print("the sum of all the numbers present is : ",sum)
print("the reverese of the number is : ",rev)
