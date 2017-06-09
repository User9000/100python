 
#
#Create a script that creates a file with each letter in the alphabet
# in each file, the letter should be added
#

import string


letters = string.ascii_lowercase

for i in letters:
    with open(str(i + ".txt"),"w") as file:
        file.write(i)
        file.close
        