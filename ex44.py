#
#   divide the string in three slices 
#   so we have 3 slices of lenght 9 
#  then we combined the three slices and iterate through the zipped list
#   we then add the three output together to the file three_letters.txt
#


import string


print(len(string.ascii_lowercase[0::3]))
print(len(string.ascii_lowercase[1::3]))
print(len(string.ascii_lowercase[2::3] + " "))

zipped = zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]+ " ")
with open("three_letters.txt","w") as file:
 for i,j,k in zipped:
    file.write(i + j + k +"\n")

