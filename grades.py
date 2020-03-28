def fun(a):
    b=[]
    d=[]
    x=[]
    for i in range (0,a):
     n=input("enter the student's name:")
     c=int(input("enter the marks of student:"))
     b.append(c)
     x.append(n)
    f=max(b)
    print("your marks","\t Student name","\tyour percentage")
    for i in range (0,a):
      g=(b[i]/f)*100
      d.append(g)
    for i in range (0,a):
      if (90<d[i]<101):
        print(b[i],"\t\t",x[i],"\t\ta+ grade")
      elif(80<d[i]<91):
        print(b[i],"\t\t",x[i],"\t\ta grade")
      elif(70<d[i]<81):
        print(b[i],"\t\t",x[i],"\t\tb+ grade")
      elif(60<d[i]<71):
        print(b[i],"\t\t",x[i],"\t\tb grade")
      elif(50<d[i]<61):
        print(b[i],"\t\t",x[i],"\t\tc+ grade")
      elif(40<d[i]<51):
        print(b[i],"\t\t",x[i],"\t\tc grade")
      elif(30<d[i]<41):
        print(b[i],"\t\t",x[i],"\t\td grade")
      else:
        print(b[i],"\t\t",x[i],"\t\tfail")
z=eval(input("enter the limit "))
fun(z)
