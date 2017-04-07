import string


with open("double_letters.txt","w") as file:
    for let1,let2 in zip(string.ascii_lowercase[0::2],string.ascii_letters[1::2]):
        file.write(let1 + let2 + "\n")

        
