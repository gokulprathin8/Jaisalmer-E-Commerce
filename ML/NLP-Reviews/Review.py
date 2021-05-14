import re

import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Importing Dataset
dataset = pd.read_json("Beauty_5.json", lines=True)

# Droping Columns
col_drop = [
    "reviewerID",
    "reviewerName",
    "helpful",
    "unixReviewTime",
    "reviewTime",
    "summary",
]

dataset.drop(columns=col_drop, axis=1, inplace=True)

# Renaming The Column Names

dataset.rename(
    columns={
        "asin": "ProductID",
        "reviewText": "Review",
    },
    inplace=True,
)

dataset["Rating"] = dataset["overall"]
dataset.drop(columns=["overall"], axis=1, inplace=True)

# Droping duplicates items
dataset.drop_duplicates(subset="ProductID", keep="first", inplace=True)
dataset.reset_index(inplace=True)
to_drop = ["ProductID", "Rating"]

X = dataset.drop(to_drop, axis=1)
y = dataset["Rating"]

# Text Cleaning


corpus = []
lematizer = WordNetLemmatizer()

sentences = X.copy()

# Getting Clean Reviews

for i in range(0, len(sentences)):
    review = re.sub("[^a-zA-Z]", " ", sentences["Review"][i])
    review = review.lower()
    review = review.split()
    review = [
        lematizer.lemmatize(word)
        for word in review
        if word not in set(stopwords.words("english"))
    ]
    review = " ".join(review)
    corpus.append(review)

# Using TF-IDF model

tfidf = TfidfVectorizer()

X_final = tfidf.fit_transform(corpus).toarray()
y_final = np.array(y)


# Splitting data into training set and test set

X_train, X_test, y_train, y_test = train_test_split(
    X_final, y_final, test_size=0.25, random_state=42
)

# Using RandomForestRegressor

regressor = RandomForestRegressor(random_state=0)
regressor.fit(X_train, y_train)

# Testing the model
y_pred = regressor.predict(X_test)

# Checking the accuracy of the model

errors = abs(y_pred - y_test)
print("Metrics for RandomForestRegressor Trained on Original Data")
# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
accuracy = 100 - np.mean(mape)
print("Accuracy:", round(accuracy, 5), "%.")
