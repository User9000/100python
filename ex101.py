

import pandas


data = pandas.read_csv("points.txt")

print(data['Score'].sum())
#for index,row in data.iterrows():
 #   row['Score'].sum