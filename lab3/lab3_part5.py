


import pandas as pd

data = pd.read_csv("IRIS.csv") # add destination for your IRIS file.

print(data.head())

print(data.species[0:51])