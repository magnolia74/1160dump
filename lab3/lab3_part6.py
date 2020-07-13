

import pandas as pd

data = pd.read_csv("/Users/Desktop/IRIS.csv")

print(data.head(52))


if data.species[50] == 'iris-versicolor':
    print('\n',"String is matched")
    print(sepal_length)
else:
    print('\n',"String is not matched")