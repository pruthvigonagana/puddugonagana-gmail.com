class A:
   def __init__(self,real,imaginary):
       self.real=real;
       self.imaginary = imaginary
   def add(self , ob):
        print(self.real+ob.real,"+",self.imaginary+ob.imaginary,"i")
   def sub(self,ob):
        print(self.real-ob.real,"+",self.imaginary-ob.imaginary,"i")
   def check(self,ob):
       if(self.real==ob.real & self.imaginary==real.imaginary):
           print("yes the complex numbers are equal")
       else :
           print("no they are'nt equal")
   def mul(self,ob):
       print((self.real*ob.real)-(self.imaginary*ob.imaginary),"+",(self.real*ob.imaginary)+(self.imaginary*ob.real),"i")
   def div(self,ob):
       print((self.real*ob.real)+(self.imaginary*ob.imaginary),"+",(self.real*ob.imaginary)-(self.imaginary*ob.real),"i","/",(ob.real**2)+(ob.imaginary**2))
def cal(z):
    x=int(input("choose any of the options:"))
    
 
    
    obj = A(c,d)
    obj2= A(a,b)
    if (x==1):
      obj.add(obj2)
    
    elif(x==2):
      obj.sub(obj2)
    
    elif(x==3):
      obj.check(obj2)
      
    elif(x==4):
      obj.mul(obj2)
      
    elif(x==5):
      obj.div(obj2)
      

print("\t welcome \t to \t complex\t numbers \t calculator")
f=1
c=int(input("enter the real part of the first complex number "))
d=int(input("enter the imaginary part of the first complex numbers "))
a=int(input("enter the real part of the second complex number "))
b=int(input("enter the imaginary part of the second complex numbers "))
print("\n1.Addition\n2.Substraction\n3.check\n4.Multiplication\n5.Division")

while(f<2):
    cal(f)

    
    
    


