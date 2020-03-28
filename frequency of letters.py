string= "Abhijeet_Joshi"
res={} 
for i in string:
    res[i] = res.get(i, 0) + 1
print ("Count : \n"+ str(res))
