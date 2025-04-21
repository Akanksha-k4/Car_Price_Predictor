from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
car = pd.read_csv('quikr_car.csv')
print(car.head())
print(car.info())
print(car.shape)


print(car['year'].unique())
print(car['fuel_type'].unique())
print(car['kms_driven'].unique())

# PROBLEMS
# -year has many non year values
# -year object to int
# -price has ask for price
# -price object to int
# -kms driven has kms with integers
# -kms driven object to int
# -kms driven has many nan values
# -fuel_type has nan values
# -keep first 3 words of name

# CLEANING OF DATA

backup = car.copy()
car = car[car['year'].str.isnumeric()]
car['year'] = car['year'].astype(int)
car = car[~car['Price'].str.contains('ask', case=False, na=False)]

car['Price'] = car['Price'].str.replace(',', '').astype(int)

print(car.info())
# 45,000 kms --so we need to remove kms and convert to int without comma
print(car['kms_driven'])

car['kms_driven'] = car['kms_driven'].str.replace(
    ',', '').str.replace('kms', '').str.strip()

car = car[car['kms_driven'].str.isnumeric()]
car['kms_driven'] = car['kms_driven'].astype(int)
print(car['kms_driven'])

car = car[~car['fuel_type'].isna()]
print(car.info())

car['name'] = car['name'].str.split(' ').str[:3].str.join(' ')
print(car['name'])

car = car.reset_index(drop=True)
print(car.head())
print(car.describe())

car = car[car['Price'] < 6e6].reset_index(drop=True)
print(car.head())

car.to_csv('cleaned_quikr_car.csv')

# MODEL BUILDING

X = car.drop(columns=['Price'])
y = car['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=433)


ohe = OneHotEncoder()
ohe.fit(X[['name', 'company', 'fuel_type']])
print(OneHotEncoder())

A = ohe.categories_

column_trans = make_column_transformer(
    (OneHotEncoder(categories=A), ['name', 'company', 'fuel_type']),
    remainder='passthrough'
)  # it will apply column transformer to the columns mentioned and pass the rest of
lr = LinearRegression()
pipe = make_pipeline(column_trans, lr)

print(pipe.fit(X_train, y_train))

y_pred = pipe.predict(X_test)
print(r2_score(y_test, y_pred))

# scores = []
# for i in range(1000):
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.2, random_state=i)
#     lr = LinearRegression()
#     pipe = make_pipeline(column_trans, lr)
#     pipe.fit(X_train, y_train)
#     y_pred = pipe.predict(X_test)
#     # print(r2_score(y_test, y_pred),i)
#     score = r2_score(y_test, y_pred)
#     scores.append(score)
#     #print(i, score)
#    # print("Best R2 Score:", max(scores))
# print("Best Random State:", scores.index(max(scores)))

import pickle
pickle.dump(pipe, open('LinearRegressionModel.pkl', 'wb'))

sample = pd.DataFrame([['Maruti Suzuki Swift', 'Maruti', 2018, 50000, 'Petrol']], columns=['name', 'company', 'year', 'kms_driven','fuel_type', ])
print(pipe.predict(sample))