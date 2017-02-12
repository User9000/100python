

a=["1",1,"1",2]
b=list(map(str,a))
c=[]
itr=0
for i in b:

    if i == b[itr+1] and itr != 0:
        continue
    else:
        c.append(a[itr])
        print("in else")
    itr=+1


print(c)
       
 
      