
import pandas


pd1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
pd2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
frames = [pd1,pd2]
together = pandas.concat(frames)
together.to_csv("concat.txt", index=None)