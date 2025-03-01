#Created on Fri May 12 18:36:12 2023

#@author: Felipe Leite


import pandas
#importing and turning categorical variables into dummy
df=pandas.read_excel("C:/Users/Felipe Leite/OneDrive/Área de Trabalho/Master UCW/Fourth Term/BUSI 652 - Predictive Analysis/Group assingment/Franchises Dataset.xlsx")
df=pandas.get_dummies(df, columns=["Location","Business Type"])

#setting variables
y = df['Net Profit']
x = df.drop('Net Profit', axis=1)

y_train = y[0:81]
x_train = x[0:81]

y_test=y[81:]
x_test=x[81:]

#Random Florest settings
from sklearn.tree import DecisionTreeRegressor
dtmodel=DecisionTreeRegressor()
dtmodel.fit(x_train,y_train)

#For error mesurament
y_pred=dtmodel.predict(x_test)
ape=abs(y_pred-y_test)/y_test*100
mape=ape.mean()
mape

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
