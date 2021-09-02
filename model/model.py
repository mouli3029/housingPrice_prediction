import pickle
import pandas as pd
import numpy as np
from sklearn import linear_model


df = pd.read_csv('housing.csv')


# Handling null values
mean_bed = df.bedrooms.mean()

df.bedrooms = df.bedrooms.fillna(mean_bed)

# Creating the model for prediction

model = linear_model.LinearRegression()
model.fit(df[['area', 'bedrooms', 'age']], df['price'])

regressor = model.predict([[3200, 4.0, 20]])


pickle.dump(model, open('model.pkl', 'wb'))


# Check
pickel_model = pickle.load(open('model.pkl', 'rb'))

print(pickel_model.predict([[3200, 4.0, 20]]))
