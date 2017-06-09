#
#write a script that iterates through each of the 26 text files, checks if the letter inside the text file is in string 
#"python" and puts the letter in a list if the letter is a charafter of "python"

import glob


string_check = "python"

file_list = glob.glob("letters/*.txt")

is_in_string = []

for i in file_list:

    with open(i, "r") as fp:
        text = fp.read().strip('\n')
        #print(text)

        if  text in string_check:
            #print("it is!")
            is_in_string.append(text)
    fp.close()

print(is_in_string)
    


