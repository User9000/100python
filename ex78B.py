
#random password generator
import random


chracters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

chosen = random.sample(chracters,6)
password = "".join(chosen)
print(password)