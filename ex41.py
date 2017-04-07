#
#Write each letter of the alphabet in a text file.
#
#
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
file = "alphabet.txt"

with open(file, "a") as fp:

    for i in a:
        fp.write(i+'\n')

fp.close

