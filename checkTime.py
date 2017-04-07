import time
import os
import datetime
print (time.ctime())

print (os.path.getmtime('ex41.py'))

print(datetime.datetime.fromtimestamp(os.path.getmtime('ex41.py')))

print(datetime.datetime.today())


#if datetime.datetime.fromtimestamp(os.path.getmtime('ex41.py') < datetime.datetime.today():
   #print ("its old!")