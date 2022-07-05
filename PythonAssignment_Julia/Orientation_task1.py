import pandas as pd
import numpy as np

ratingsInput = pd.read_csv('RatingsInput.csv')

ratingsInput["MovieID"] = ratingsInput["MovieName"].str.split(',').str.get(0)
ratingsInput["MovieName"] = ratingsInput["MovieName"].str.split(',').str.get(1)


print(ratingsInput.head(15))

