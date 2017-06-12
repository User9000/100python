import requests


r = requests.get("http://www.pythonhow.com/universe.txt")
print(r.text)