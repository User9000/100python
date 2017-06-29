

checklist = ["Portugal", "Germany", "Munster", "Spain"]



file = open("newCountries2.txt", 'r')

new_checklist = []
for line in file.readlines():
    print(type(line))
    if line.rstrip() in checklist:
        new_checklist.append(line.rstrip())
        





print(new_checklist)