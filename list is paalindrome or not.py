def fun(a):
    b=a[::-1]
    if(b==a):
        print(" List is Palindrome")
        return True
    else:
        print(" List is not Palindrome")
        return False
    print(b)
c=[1,2,2,1]
d=fun(c)
print(d)

