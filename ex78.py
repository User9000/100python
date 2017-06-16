

#Password generator that generates a password of a random alphanumeic chracters in the range

import string
import random
random_string = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%^&*()?'

itr = 0
password =""
while itr < 6:
    number= random.randint(0,74)
    password =password + random_string[number]
    itr = itr + 1

print (password)


       



