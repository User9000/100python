


with open("user_data_.txt", "a") as fd:


    while (True):
         word = input("Write value: ")
         if word == "CLOSE":
            break
         for i in word.split():
             fd.write(i + "\n")


