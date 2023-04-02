# @Time    : 3/29/2023 5:58 PM
# @Author  : Pronob Barman
# @FileName: test3.py
# @Software: PyCharm

import pandas as pd

# read csv file
data = pd.read_csv('data.csv', encoding='Windows-1252')

# select columns that start with Q84 or Q85
# filtered_data = data.filter(regex='^(Q84|Q85)')
filtered_data = data.filter(regex='^Q84', axis = 1)

# print filtered columns
# print(filtered_data.columns)

# import pandas as pd

# # read the CSV file into a pandas dataframe
# df = pd.read_csv('data.csv')
#
# # filter the columns that start with Q84 or Q85
# q84_q85_cols = [col for col in df.columns if col.startswith(('Q84', 'Q85'))]
#
# # create a new dataframe with only the selected columns
# df_q84_q85 = df[q84_q85_cols]

import os
import matplotlib.pyplot as plt

# create the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# loop through each column in the dataset
for col in filtered_data.columns:
    # if column is numerical, create a histogram
    if filtered_data[col].dtype in ['int64', 'float64']:
        plt.hist(filtered_data[col])
        plt.title(col)
        plt.savefig(f"plots/{col}.png")
        plt.show()
    # if column is categorical, create a bar plot
    else:
        filtered_data[col].value_counts().plot(kind='bar')
        plt.xticks(rotation=75)  # rotate the tick labels by 45 degrees
        plt.title(col)
        plt.ylabel('Count')
        plt.tight_layout()  # adjust the layout to prevent overlapping labels
        plt.savefig(f"plots/{col}.png")
        plt.show()
