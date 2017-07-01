#submit 

import os

def user_input():
    word = input("Enter a word: ")
    return word

with open("data_from_user.txt","a+") as fd:
    while True:
        word = user_input()
        if word == "CLOSE":
                fd.close()
                break
        elif word == "SAVE":
            fd.flush()
            os.fsync(fd)     
        else:
            fd.write(word + "\n")
  