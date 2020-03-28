a=eval(input("enter no. of units consumed by the user:- "))
if a>=1 and a<=100:
    e=a*1.5+25
elif a>=101 and a<=200:
    e=100*1.5+(a-100)*2.5+50
elif a>=201 and a<=300:
    e=100*1.5+100*2+(a-200)*4+75
elif a>=301 and a<=400:
    e=100*1.5+100*2+100*4+(a-300)*7+100
else:
    e=4000
print("total electiricty bill:-",e)
