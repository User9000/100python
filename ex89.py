
#Get countries greater than 2,000,000.

import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("SELECT country FROM countries WHERE area > '2000000' ")



for i in c.fetchall():
      
      print(i[0])