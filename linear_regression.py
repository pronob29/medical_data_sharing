# @Time    : 4/2/2023 2:44 PM
# @Author  : Pronob Barman
# @FileName: linear_regression.py
# @Software: PyCharm

'''
This script is used to perform linear regression on the techScore data
'''

# import libraries
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


# read csv file
data = pd.read_csv('linear_regression.csv')

# print(data.head())

# print(data.columns)

# drop rows with missing values
data.dropna(inplace=True)

# create dummy variables for the 'race' column
# race_dummies = pd.get_dummies(data['race'], prefix='race')
# concatenate the dummy variables with the original data
# data = pd.concat([data, race_dummies], axis=1)

# drop the original 'race' column
data.drop('race', axis=1, inplace=True)

# response variable
y = data['techScore']
# predictor variables
x = data.iloc[:, 1:]
print(x.head())
# split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# fit the model
regressor = LinearRegression()
model = regressor.fit(x_train, y_train)

# print the coefficients
print("Model Coefficient:", model.coef_)
print("Model Intercept: ", model.intercept_)
# print the score or r-squared value
print("R-squared value: ", model.score(x_test, y_test))
# print the predictions for the test set
y_pred = model.predict(x_test)
print("y predicted values: ", y_pred)

# generate and print model summary using statsmodels
X_train = sm.add_constant(x_train) # add a constant term for intercept
model_sm = sm.OLS(y_train, x_train).fit()
print(model_sm.summary())

# add constant term to test data
X_test = sm.add_constant(x_test)
# predict response variable on test data using fitted model
y_pred = model_sm.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("R-squared value: ", r2)
# print intercept and coefficients
print('Intercept:', model_sm.params[0])
print('Coefficients:')
print(model_sm.params[1:])

# generate and print model summary
print(model_sm.summary())


# plot the residuals vs predicted values
plt.scatter(y_pred, y_pred - y_test)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Values')
plt.show()

# create a file object
with open('linear_regression_results.txt', 'w') as f:
    # write the model coefficients to the file
    f.write('Model Coefficients: {}\n'.format(model.coef_))

    # write the model intercept to the file
    f.write('Model Intercept: {}\n'.format(model.intercept_))

    # write the r-squared value to the file
    # f.write('R-squared value: {}\n'.format(model.score(x_test, y_test)))

    # write the predictions for the test set to the file
    # f.write('Predicted Values: {}\n'.format(y_pred))
    # write the intercept to the file
    f.write('Intercept:{}\n'.format(model_sm.params[0]))
    # write the model summary to the file
    f.write('{}\n'.format(model_sm.summary()))
