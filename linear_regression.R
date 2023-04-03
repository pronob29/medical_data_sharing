# load the necessary libraries
library(readr)
library(dplyr)
library(caret)
library(car)
library(ggplot2)
library(MASS)

# read in your dataset
df <- read_csv("C:/tera reynolds/techscore.csv")
head(df)
# set the independent variables (X) and dependent variable (y)
X <- subset(df, select = c(otherPHR, PP, thirdParty, miPHR, selfTrackingApp, homeMedDevice, wearable))
y <- df$techScore

# split the dataset into train and test sets with a 70-30 ratio
set.seed(42)
train_index <- createDataPartition(y, p = 0.8, list = FALSE)
X_train <- X[train_index, ]
X_test <- X[-train_index, ]
y_train <- y[train_index]
y_test <- y[-train_index]

# fit the multiple linear regression model on the training set
model <- lm(y_train ~ ., data = cbind(X_train, y_train))

# predict the response variable on the test set
y_pred <- predict(model, newdata = X_test)

# calculate the mean squared error and mean absolute error
mse <- mean((y_test - y_pred)^2)
mae <- mean(abs(y_test - y_pred))

print(paste("Mean Squared Error:", mse))
print(paste("Mean Absolute Error:", mae))

# print the model summary
summary(model)

# create a data frame of predicted and actual values
residuals_df <- data.frame(y_pred = y_pred, y_actual = y_test, residual = y_test - y_pred)

# plot residuals vs predicted values
ggplot(residuals_df, aes(x = y_pred, y = residual)) +
  geom_point() +
  geom_hline(yintercept = 0, linetype = "dashed") +
  xlab("Predicted Values") +
  ylab("Residuals") +
  ggtitle("Residuals vs Predicted Values")

# create a data frame with predicted and actual values
df_results <- data.frame(y_actual = y_test, y_predicted = y_pred)

# plot predicted vs. actual values
ggplot(df_results, aes(x = y_predicted, y = y_actual)) +
  geom_point() +
  geom_abline(intercept = 0, slope = 1, color = "red") +
  labs(x = "Predicted values", y = "Actual values", title = "Predicted vs. Actual values")
