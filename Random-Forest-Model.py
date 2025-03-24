#@uthor: Felipe Leite

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_percentage_error

#importing and turning categorical variables into dummy
df = pd.read_excel("C:/Users/Felipe Leite/OneDrive/Área de Trabalho/github_profile/Cafe-Profit-Forecast/Dataset/Franchises_Dataset_felipe_v.1.xlsx")
df = pd.get_dummies(df, columns=["Location","Business Type"])

#setting variables
y = df['Net Profit']
x = df.drop('Net Profit', axis=1)

y_train = y[0:81]
x_train = x[0:81]

y_test=y[81:]
x_test=x[81:]

#Random Forest settings
dtmodel=DecisionTreeRegressor()
dtmodel.fit(x_train,y_train)

#For error measurement
y_pred = dtmodel.predict(x_test)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f"MAPE: {mape}%")

#means
df["Counter Sales"].mean()
df["Drive-through Sales"].mean()
df["number of customers"].mean()
df["Location_Richmond"].mean()
df["Location_Vancouver"].mean()
df["Business Type_Burger store"].mean()
df["Business Type_Café"].mean()
df["Business Type_Pizza Store"].mean()

#First prediction of the model
dtmodel.predict([[0.5,0.7,99.76,1,0,0,0,1]])
