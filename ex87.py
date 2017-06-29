

countries=["Spain", "Portugal", "Germany"]

file = open("countries-missing.txt", 'r')

file = [i.rstrip() for i in file.readlines()]

for i in countries:
    if i not in file:
        file.append(i)

file.sort()

with open("no-missing-countries.txt",'w') as fd:
    
    for i in file:
        fd.write(i.rstrip() + "\n")


