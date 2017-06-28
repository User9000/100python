
#Open new file for redirection of clean data
theother = open("newCountries2.txt",'w')
#Open file with dirty data
with open("countries-raw.txt") as file:
    fd = file.readlines()
# itereate and get garbage chars of 1 and 2 out!
list1= [i for i in fd if (len(i) != 1 and len(i) != 2)]
#iterae to the string and get the \n out!
for i in list1:
   if i.rstrip() != "Top of Page":
       theother.write(i.rstrip() + "\n")
file.close()
theother.close()