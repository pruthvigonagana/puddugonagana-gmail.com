lis=['a','e','i','o','u']
string=input("enter the string")
a=string.lower()
print(a)
for j in range(0,len(a)):
  for i in lis:
    if a[j]==i:
       a=a.replace(a[j],"_")
print(a)
    




                        
                     
                
                
                
                  
