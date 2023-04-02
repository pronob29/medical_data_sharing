# @Time    : 3/29/2023 5:58 PM
# @Author  : Pronob Barman
# @FileName: sentiment_analysis.py
# @Software: PyCharm

'''
This script is used to perform sentiment analysis on the data collected from the survey. (Q85)
Used nltk library to perform sentiment analysis.
'''


import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

sentences = pd.read_excel('test.xlsx')['Q85'].tolist()
sentiment_table = pd.DataFrame(columns=['sr. no', 'sentence', 'aspect', 'sentiment score', 'label'])

summary_rows = []
for i, sentence in enumerate(sentences):
    aspect_scores = {}
    sid = SentimentIntensityAnalyzer()
    for aspect in ['cost', 'benefits', 'personal medical information','security risk', 'Convenience, accessibility, and time-saving', 'data vulnerability',
                   'helpful and valuable' , 'risk', 'privacy', 'wrong hands', 'privacy and security', 'trust' ,
                   'third-party app', 'access', 'apple health records', 'CommonHealth', 'government takeover',
                   'covid corruption']:
        if aspect in str(sentence):
            sentiment_score = sid.polarity_scores(sentence)['compound']
            aspect_scores[aspect] = sentiment_score
    if aspect_scores:
        aspect = max(aspect_scores, key=aspect_scores.get)
        sentiment_score = aspect_scores[aspect]
        label = 'positive' if sentiment_score > 0 else 'negative'
        summary_rows.append({
            'sr. no': i+1,
            'sentence': sentence,
            'aspect': aspect,
            'sentiment score': sentiment_score,
            'label': label
        })
# concantenate the summary table with the new rows
sentiment_table = pd.concat([sentiment_table, pd.DataFrame(summary_rows)])
sentiment_table.to_csv('sentiment_table.csv', index=False)
# print sentiment table
print(sentiment_table)
