

import pandas as pd

data = pd.read_csv("pandas") #PANDAS destination

highest_profit = 0
second_profit = 0

movies = []

for index, row in data.iterrows():
    profit = row ["Revenue"] - row["Budget"]
    if profit > highest_profit:
        second_profit = highest_profit
        highest_profit = profit
        movies.append(row["Movie"])
    else:
        if profit > second_profit:
            second_profit = profit
            movies.insert(len(movies)-1,row["Movie"])

print(" is the movie with second highest profit".format(movies[-2],second_profit))

