
file = 'words1.txt'

with open(file,"r") as fp: 
    #read file and pass it to variable fileData
    fileData = fp.read()
    fileData = fileData.replace(","," ")
    #split words by space " "
    strings = fileData.split(" ")
    


    print(len(strings))
