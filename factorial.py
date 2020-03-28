def fact(a):
 fact=1
 for i in range(a,0,-1):
    fact=fact*a
    a=a-1
 print(fact)
b=int(input("enter the number you want to find the factorial of"))
fact(b)
    
    
