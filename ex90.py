import sqlite3
import csv

#Get countries greater than 2,000,000.
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("SELECT * FROM countries WHERE area > '2000000' ")
with open("countries-200m.csv", "w") as fd:
   writer = csv.writer(fd)
   writer.writerows(c.fetchall())



       
      