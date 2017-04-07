import string


alf = len(string.ascii_lowercase)
with open('doubles.txt','w') as fp:
    for i in range(alf-1):
        j = int(i +  1)
        fp.write(string.ascii_lowercase[i] + string.ascii_lowercase[j] + "\n")
        i = i + 2
        