year=int(input("enter the current year"))
def leap(y):
    if y%400==0:
        return 'true'
    elif y%4==0:
            return 'true'
if leap(year)=='true':
    print("next 15 years are")
    for i in range(2,16):
              year=year+4
              print(year)
else:
   print("next 15 years are")
for i in range(1,5):
        if leap(year)=='true':
            for i in range(1,16):
                print(year)
                year=year+4
            break
        else:
            year=year+1
            
