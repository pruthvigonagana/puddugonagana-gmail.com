def fib(x):
    if x<=1:
        return x
    else :
        return (fib(x-1)+fib(x-2))
a=eval(input("enter the number"))
for i in range(a):
       print(fib(i))
