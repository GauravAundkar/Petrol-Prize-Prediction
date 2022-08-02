# -*- coding: utf-8 -*-
"""Petrol Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A2chi8g8h77uP6HXibEWOBzH19YHJRg4
"""

import numpy as np
import pandas as pd

df = pd.read_csv('fuel_prices.csv')

df.drop(['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3'], axis= 1,inplace=True)

df.columns = df.iloc[0]

df.drop([0,1],axis=0,inplace=True)

df1 = df.drop(['Date','Day','Moving Avg','Diesel Price','Barrel Cost'],axis=1,inplace=True)

y = df['Petrol Price']
x = df.drop(['Petrol Price'],axis =1)

# from sklearn.preprocessing import MinMaxScaler
# sc = MinMaxScaler()
# x1=sc.fit_transform(x)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x.values,y)
# print(model.predict([[66,44]]))
# model.predict(x_test)

# print(model.score(x_test,y_test))

# from sklearn.metrics import mean_absolute_error,mean_squared_error
#
# mae = mean_absolute_error(y_test,y_predicted)
# mse = mean_squared_error(y_test,y_predicted)
#
# print("Mean absolute error : ",mae)
# print("Mean squared error : ",mse)