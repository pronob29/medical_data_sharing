'''
Third party app data sharing response of the participants
here we make a list of columns that start with Q84
then we melt the dataframe to create one column for all categorical variables
then we count occurrences of each category and store in new dataframe
then we print the counts dataframe
then we create a bar plot for each categorical variable
then we save the bar plot as a png file in the plots folder
'''




# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt

# read csv file
data = pd.read_csv('data.csv', encoding = 'Windows-1252')

# select columns that start with Q84
filtered_data = data.filter(regex = '^Q84', axis = 1)

# create the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# define the order of categories for each variable
category_order = [
            'Very Comfortable', 'Comfortable', 'Neutral',
            'Uncomfortable', 'Very Uncomfortable'
                ]

for col in filtered_data.columns:
    # if column is numerical, create a histogram
    if filtered_data[col].dtype in ['int64', 'float64']:
        plt.hist(filtered_data[col])
        plt.title(col)
        plt.savefig(f"plots/{col}.png")
        plt.show()
    # if column is categorical, create a bar plot
    else:
        # get the order of categories for this variable
        # get the order of categories for this variable
        category_order_all = {}
        category_order_all[col] = category_order

        # create the bar plot using the specified category order
        try:
            filtered_data[col].value_counts().loc[category_order_all[col]].plot(kind = 'bar')
        except KeyError as e:
            print(f"Error: {e}")  # print the error
            continue  # skip this column if there is an error

        plt.xticks(rotation = 45)  # rotate the tick labels by 45 degrees
        plt.title("Data Sharing Distribution")  # use consistent title formatting
        plt.ylabel("Count")
        plt.tight_layout()  # adjust the layout to prevent overlapping labels
        plt.savefig(f"plots/{col}.png")
        plt.show()
