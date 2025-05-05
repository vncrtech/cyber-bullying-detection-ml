import pickle
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# opens the initial training file
DATASET = "training_dataset.csv"
train_data = pd.read_csv(DATASET, encoding='ISO-8859-1')

train_data['classification 2'] = train_data['classification 2'].replace(
    'Bully', 1)
train_data['classification 2'] = train_data['classification 2'].replace(
    'Not bully', 0)

# Sets the X and y values. X = input, y = prediction
X = train_data
y = train_data['classification 2']

vect = CountVectorizer(ngram_range=(1, 5), max_df=0.99)

X_dtm = vect.fit_transform(X.text)

nb = MultinomialNB(alpha=0.001)
nb = nb.fit(X_dtm, y)

model_file = "trained_model.sav"
pickle.dump(nb, open(model_file, 'wb'))

vect_file = "vect.sav"
pickle.dump(vect, open(vect_file, 'wb'))
