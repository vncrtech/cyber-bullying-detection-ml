import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

model_file = 'trained_model.sav'
loaded_model = pickle.load(open(model_file, 'rb'))

predict_file = 'tweets.csv'
new_data = pd.read_csv(predict_file) #enconding = 'ISO-8859-1'

input_text = new_data['Text']

vect = CountVectorizer(ngram_range=(1,5), max_df=0.99)
X_dtm = vect.transform(input_text)
# y_predicted = loaded_model.predict(X_dtm)
#
# predictions = pd.concat([input_text,pd.DataFrame(y_predicted)],axis=1)
#
# predictions.to_csv('predictions.csv', encoding='utf-8')

