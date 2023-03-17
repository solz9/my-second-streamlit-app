import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('IceCreamData.csv')
df.head()
x1 = df['Temperature'].values
y1 = df['Revenue'].values

x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size = 50/500) 
model = LinearRegression()
x_train = x_train.reshape(-1, 1)
model.fit(x_train, y_train)
filename = 'model.pickle'
pickle.dump(model, open(filename, 'wb'))
