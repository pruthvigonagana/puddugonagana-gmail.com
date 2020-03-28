def check(x,y):
    if(x==y):
        return 1
    else:
        return 0

a=eval(input("enter the first number"))
b=eval(input("enter the second number"))
c=check(a,b)
if (c==1):
    print("same")
else :
    print("not same")
