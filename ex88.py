
import pandas

df = pandas.read_csv("countries-by-area.txt")
df1= df['population_2013']/df["area_sqkm"]
dfinal = df1.nlargest(5)

for i in dfinal.index:
    print(df["country"].iloc[i])




