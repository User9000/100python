

#Get screen resolution with python

from win32api import GetSystemMetrics

print("width", GetSystemMetrics(0))
print("height",GetSystemMetrics(1))