

#Get the score of all points !

import pandas


data = pandas.read_csv("points.txt")

print(data['Score'].sum())
