

#d =[{ "wheather":}]
#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def check(var1):
    print(d[var1])


var2 = input("Enter the word: ")


try:
    check(var2)

except KeyError:
    print ("I do know that word!")

