k = 6
for i in range(0, 7): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1
        for j in range(0, i+1):
            if (i %2!=0):
                continue
            print("* ", end="") 
        print("\r")
l=3
print("\r")
for i in range(5, -1,-1): 
        for j in range(l, 1,-1): 
            print(end=" ") 
        l = l+1
        for j in range(i-1,-1,-1):
            if (i %2==0):
                continue
            print("* ", end="") 
        print("\r")
