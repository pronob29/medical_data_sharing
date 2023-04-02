import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

sentences = pd.read_excel('test.xlsx')['Q85'].tolist()
summary_table = pd.DataFrame(columns=['sr. no', 'sentence', 'aspect', 'sentiment score', 'label'])

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
summary_table = pd.concat([summary_table, pd.DataFrame(summary_rows)])
summary_table.to_csv('summary_table.csv', index=False)

print(summary_table)
