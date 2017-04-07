import string


with open("letters.txt","w") as fp:
    for letter in string.ascii_lowercase:
        fp.write(letter + "\n")

fp.close
