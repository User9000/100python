import requests
import pandas
from io import StringIO
import numpy
data = requests.get("http://www.pythonhow.com/data/sampledata.txt").text

dp = pandas.read_csv(StringIO(data))


dp = 2*dp
numpy.savetxt('pandas.txt',dp.values, fmt='%d',delimiter="\t", header="X\tY")



