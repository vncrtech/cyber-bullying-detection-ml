import pickle
import pandas as pd

model_file = 'trained_model.sav'
model = pickle.load(open(model_file, 'rb'))

vect_file = 'vect.sav'
vect = pickle.load(open(vect_file, 'rb'))

PREDICT_FILE = 'tweets.csv'

# Specify the encoding to handle special characters
# Use 'latin1' or 'ISO-8859-1' if UTF-8 fails
new_data = pd.read_csv(PREDICT_FILE, encoding='latin1')

input_text = new_data['Text']
# Handle NaN values by replacing them with an empty string
input_text = input_text.fillna('')

X_dtm = vect.transform(input_text)
y_predicted = model.predict(X_dtm)

predictions = pd.concat([input_text, pd.DataFrame(y_predicted)], axis=1)
predictions.columns = ['Text', 'Prediction']
predictions['Prediction'] = predictions['Prediction'].replace(1, 'Bully')
predictions['Prediction'] = predictions['Prediction'].replace(0, 'Not Bully')

predictions.to_csv('predictions.csv', encoding='utf-8', index=False)
