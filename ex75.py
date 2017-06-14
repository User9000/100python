import pandas
from bokeh.plotting import figure, output_file, show


pd1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

p = figure(plot_width=400, plot_height=400, title=None, toolbar_location="below")
p.triangle(x=pd1['x'], y=pd1['y'], size=20, color="#F0027F")

show(p)