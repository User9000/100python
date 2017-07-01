

#create a file that is sepated by commas.

values = input("Enter values: ")



print(values.split(","))

with open("planets.txt", "a") as fd:
    for i in values.split(","):
        fd.write(i + "\n")