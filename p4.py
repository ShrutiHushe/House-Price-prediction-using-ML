# model creation

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import *

data = pd.read_csv("abp_march24.csv")

features = data[["area", "bedrooms"]]
target = data["price"]

x_train, x_test, y_train, y_test = train_test_split(features.values, target, random_state=19)

model = LinearRegression()
model.fit(x_train, y_train)

f = open("hpp.pkl", "wb")
dump(model, f)
f.close()