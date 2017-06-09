#write a script that extracts letters from the 26 text files and put the letters in a list.

import os

textfiles = os.listdir(".")
listOfLetters = []

for i in textfiles:
    if ".txt" in i:
        with open(i, "r") as fp:
            text = fp.read()
            print(text)
            fp.close()

