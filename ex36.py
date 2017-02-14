file = 'words1.txt'

with open(file,"r") as fp:
    fileData = fp.read()
    strings = fileData.split(" ")

    print(len(strings))



