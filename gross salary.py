a=eval(input("enter a number"))
if a>100000:
    basic=4000
    hra=20*4000/100
    da=110*4000/100
    cong=500
    incentive=10*a/100
    bonus=1000
else:
    basic=4000
    hra=10*4000/100
    da=110*4000/100
    cong=500
    incentive=4*a/100
    bonus=500
total=basic+hra+da+cong+incentive+bonus
print("your total salary is :",total)
