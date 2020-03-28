d={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
c=input("enter the octal number ")
for i in range (0,len(c)):
    f=c[i]
    print(d[f],end="")
