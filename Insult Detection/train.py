import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# opens the initial training file
train_file = "training_dataset.csv"
train_data = pd.read_csv(train_file,encoding='ISO-8859-1')

# Sets the X and y values. X = input, y = prediction
X = train_data
y = train_data['classification 2']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

vect = CountVectorizer(ngram_range=(1,5), max_df=0.99)

X_dtm = vect.fit_transform(X.text)

nb = MultinomialNB(alpha=0.001)
nb = nb.fit(X_dtm, y)

save_file = "trained_model.sav"
pickle.dump(nb, open(save_file, 'wb'))