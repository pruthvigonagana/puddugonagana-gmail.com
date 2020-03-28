def gcd(a,b):
 if b == 0:
    return a
 else:
    return gcd(b,a%b)
a=eval(input("enter first number= "))
b=eval(input("enter second number= "))
x=gcd(a,b)
print("gcd of ",a," and ",b," is= ", x)
