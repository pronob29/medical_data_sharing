# @Time    : 4/6/2023 1:03 PM
# @Author  : Pronob Barman
# @FileName: health_literacy.py
# @Software: PyCharm

'''
This script is about making a health literacy score for the participants from  the survey questions Q88 to Q91.
Health literacy Score (Index?) --> no knowledge (0) to Very knowledgeable(100)
help from someone in reading (Q88) - always (1), 2, 3, 4, never (5)
self-confidence level- (Q89) - not at all (1), 2, 3, 4, extremely (5)
Difficulty of understanding written information (Q90) - always (1), 2, 3, 4, never (5)
Difficulty of understanding medical terms in speaking (Q91) - always (1), 2, 3, 4, never (5)
'''

# import libraries
import pandas as pd

# Step 1: Load the data
df = pd.read_csv('data.csv', encoding='Windows-1252')

# Step 2: Select the columns of interest
cols = ['Q88', 'Q89', 'Q90', 'Q91']
data = df.loc[:, cols]

# Step 3: Convert values to numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Step 4: Calculate the sum of the values in each row
scores = data.sum(axis=1)

# Step 5: Calculate the percentage score
health_literacy_score = (scores / 20) * 100

# print(health_literacy_score)
# Add the health literacy score to the dataframe
techscore = pd.read_csv('techscore.csv')
techscore['health_literacy_score'] = health_literacy_score

race = df['Q98']
response = race.values.tolist()

white_categories = ["White"]
black_categories = ["Black or African American"]
other_categories = ["American Indian or Alaska Native", "Asian", "Hispanic or Latino", "Middle Eastern",
                    "Native Hawaiian or Pacific Islander", "Prefer not to disclose", "Prefer to self-describe:",]

new_race = []

for i, r in enumerate(response):
    if r in white_categories or r.startswith("White,"):
        new_race.append("White")
    elif r in black_categories:
        new_race.append("Black")
    elif any(r.startswith(x) for x in other_categories):
        new_race.append("Other")
    # else:                 # it will print the invalid responses with the index number
    #     print("Invalid response at index {}: {}".format(i, r))

techscore['race'] = new_race
print(techscore)