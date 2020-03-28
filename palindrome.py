sum=0
a=eval(input("enter the number"))
b=a
while a>0:
    d=a%10
    sum=sum*10+d
    a=a//10
if b==sum:
    print("yes the number is an palindrome")
else:
    print("no it is not a palindrome")
