# @Time    : 4/1/2023 11:59 PM
# @Author  : Pronob Barman
# @FileName: q84.py
# @Software: PyCharm

# making a list of columns that start with Q84
import pandas as pd

# read csv file
data = pd.read_csv('data.csv', encoding='Windows-1252')

# select columns that start with Q84 or Q85
# filtered_data = data.filter(regex='^(Q84|Q85)')
filtered_data = data.filter(regex='^Q84', axis = 1)
# melt dataframe to create one column for all categorical variables
melted_df = pd.melt(filtered_data, var_name='Variable', value_name='Category')

# count occurrences of each category and store in new dataframe
counts_df = melted_df.groupby(['Variable', 'Category']).size().reset_index(name='Count')
counts_df.to_csv('counts.csv', index=False)
# print counts dataframe
print(counts_df)