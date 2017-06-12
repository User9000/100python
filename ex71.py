import requests


r = requests.get("http://www.pythonhow.com/data/universe.txt")
lists1= []
for i in r.text.lower():
    if i == 'a':
        lists1.append(i)
print(len(lists1))