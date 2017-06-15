import time

var1 = int(time.strftime("%Y",time.gmtime()))

userAge= int(input("Whats your age?"))

born = var1 - int(userAge)

print("You were born in  {bornyear}".format(bornyear=born) )

