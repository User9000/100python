from datetime import datetime


age = inp(input("What's your age? "))
year_birth = datetime.now().year - age

print("You were born back in %s" % year_birth)