
import sqlite3
import pandas


conn = sqlite3.connect("database.db")
cur= conn.cursor()

data = pandas.read_csv('ten-more-countries.txt')

for index, row in data.iterrows():
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)", (row["Country"], row["Area"]))



conn.commit()
conn.close()


