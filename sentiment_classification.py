import pandas as pd
import re
from nltk.corpus import stopwords
from textblob import TextBlob
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load the data into a Pandas DataFrame
df = pd.read_excel('test.xlsx')
# Clean the data.
df = df.dropna()
df = df.drop_duplicates()
df = df.reset_index(drop=True)

# Convert to lowercase
text = df['Q85'].str.lower()
# # Remove number
text = text.map(lambda x: re.sub('[0123456789]', ' ', str(x)))
# # Remove stopwords
stop_words = stopwords.words('english')
text = text.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
# Remove punctuation except (') mark
text = text.map(lambda x: re.sub('[!"#$,%&\()*+./:!?<=>@[\\]^_{|}~;-]', ' ', x))
#remove stopwords second times
text = text.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
# Remove punctuation (') mark
text = text.map(lambda x: re.sub('[\']', ' ', x))


# Define a function for sentiment analysis
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

# Apply the get_sentiment function to the 'preprocessed_text' column of the DataFrame
df['sentiment'] = text.apply(get_sentiment)
# create a new column for sentiment labels based on polarity scores
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
# Add the preprocessed text to the DataFrame
df['text'] = text
#drop the Q85 column
df = df.drop(labels = ['Q85'], axis=1)
# make a bar chart of sentiment labels
# plot showing the distribution of sentiment labels
df['sentiment_label'].value_counts().plot(kind='bar', title='Sentiment Label Distribution')
plt.xlabel('Sentiment Label')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('sentiment_label_distribution.png')
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment_label'], test_size=0.2, random_state=42)

# Convert the text data into a matrix of token counts using CountVectorizer
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
clf1 = MultinomialNB()
clf1.fit(X_train_counts, y_train)
y_pred1 = clf1.predict(X_test_counts)

# Train a Random Forest classifier
clf2 = RandomForestClassifier(n_estimators=100)
clf2.fit(X_train_counts, y_train)
y_pred2 = clf2.predict(X_test_counts)

# Calculate the evaluation metrics
nb_accuracy = round(accuracy_score(y_test, y_pred1), 4)
nb_precision = round(precision_score(y_test, y_pred1, average='weighted'), 4)
nb_recall = round(recall_score(y_test, y_pred1, average='weighted'), 4)
nb_f1 = round(f1_score(y_test, y_pred1, average='weighted'), 4)

rf_accuracy = round(accuracy_score(y_test, y_pred2), 4)
rf_precision = round(precision_score(y_test, y_pred2, average='weighted'), 4)
rf_recall = round(recall_score(y_test, y_pred2, average='weighted'), 4)
rf_f1 = round(f1_score(y_test, y_pred2, average='weighted'), 4)

# Save the evaluation metrics to a CSV file
metrics_df = pd.DataFrame({
    'Model': ['Multinomial Naive Bayes', 'Random Forest'],
    'Accuracy': [nb_accuracy, rf_accuracy],
    'Precision': [nb_precision, rf_precision],
    'Recall': [nb_recall, rf_recall],
    'F1 Score': [nb_f1, rf_f1]
})

metrics_df.to_csv('metrics.csv', index=False)
