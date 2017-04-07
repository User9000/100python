
# Sum of each of the member of the list
#utilization of the built in function zip() to combine both lists into one.
#

a = [1,2,3]
b = (4,5,6)

#list2 = a + b
zipped = zip(a,b)
print(zipped)

for i,j in zipped:
    #print(i,j)
    print(i+j)

