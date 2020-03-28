print("*******************************************************************************")
print("**********************************ABC HOTEL*************************************")
name=(input("enter name\t"))
age=int(input("enter age\t"))
print("choose your staying class")
print("enter the hotel you want to choose")
d = eval(input('press 1 if you want the golden package @10,0000/night \npress 2 if you want the silver package @7000/night \npress 3 if want the bronze package @4000/night \nplease enter your choice : '))
if d==1:
    print('thanks for choosing golden package \nyou can get the following services \nnote: the bils of special services are to paid sepearetely they are not included in the bill')
    print('spa @600/per person \nlaundry @300/per wash \nbar5000 unlimited /night \nmassage @2000/per person ')
    a=int(input("enter number of days for stay="))
    if a==0:
          print("thankyou for your time")
          exit(0)
    else:
          s=int(input("enter no. of night for spa="))
          l=int(input("enter no. of days for laundry="))
          b=int(input("enter no. of night for bar="))
          m=int(input("enter no. of person for massage="))
          total=(a*10000)+(500*s)+(300*l)+(5000*b)+(2000*m)
         
elif d==2:
     print("welcome to silver class")
     print("you can get the folowing services : \nlunch @250/person \ndinner/person @350 \nlaunndry @150/person \nrented beds @1250/night")
     a=int(input("enter number of days for stay"))
     if a==0:
         print("thankyou for your time")
         exit(0)
     else:
         lu=int(input("enter no. of lunch for person="))
         di=int(input("enter no. of dinner per person="))
         la=int(input("enter no. of days for laundry="))
         be=int(input("enter no. of nights for beds="))
         total=(a*7000)+(250*lu)+(350*di)+(150*la)+(1250*be)
       
elif d==3:
    print("welcome to bronze class")
    print("you can get the foolowing facilities in bronze: \nbreakfast @100/per person \ncar @200/per person \nhot water @50/per person")
    a=int(input("enter number of days for stay="))
    if a==0:
         print("thankyou for your time")
         exit(0)
    else:
        br=int(input("enter no. of breakfast for person="))
        ca=int(input("enter no. of car per person="))

        h=int(input("enter no. of person for hot water="))
        total=4000+(100*br)+(200*ca)+(50*h)
       
else:
    print("invalid input")
    exit(0)

print("name:",name,"\nage:",age)
print("bill amount is:",total)
print("   ------------------------------------------plz pay your bill----------------------------------------")
print("  -----------------------------------------------------------------------------------------------------")
print(" ---------------------------------------------------thankyou visit again--------------------------------")
print("---------------------------------------------------------------------------------------------------------")
