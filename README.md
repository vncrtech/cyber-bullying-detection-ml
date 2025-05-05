# Cyberbullying Detection System

This project is an AI-based system designed to detect cyberbullying in text data. It leverages machine learning techniques to classify text as either "Bully" or "Not Bully" and provides tools for training, prediction, and visualization.

## Features
- **Training Module**: Train a Naive Bayes model using a labeled dataset ([`Core/train.py`](bullying_detection/core/train.py)).
- **Prediction Module**: Predict whether text data contains bullying content ([`Core/predict.py`](bullying_detection/core/predict.py)).
- **Twitter Streaming**: Collect and process tweets, visualize them on a map ([`Core/twitter_streaming.py`](bullying_detection/core/twitter_streaming.py)).
- **Visualization**: Generate an interactive map showing tweet locations and their content.

## Project Structure
```
Insult Detection/
├── Core/
│   ├── predict.py              # Script for making predictions
│   ├── train.py                # Script for training the model
│   ├── training_dataset.csv    # Dataset for training
│   ├── twitter_streaming.py    # Script for collecting and visualizing tweets
├── trained_model.sav           # Pre-trained model file
```

## How to Use

Perform the following commands in the [`Core`](bullying_detection/core) directory:
```bash
cd bullying_detection/core
```

1. **Train the Model**:
   Run the training script to generate a model:
   ```bash
   python train.py
   ```

2. **Make Predictions**:
   Use the prediction script to classify text data:
   ```bash
   python predict.py
   ```

3. **::DEPRECATED:: Visualize Tweets**:
   Collect tweets and visualize them on a map:
   ```bash
   python twitter_streaming.py
   ```

## Requirements
- Python 3.x
- Required libraries: `pandas`, `scikit-learn`, `folium`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Future Improvements
- Enhance the model with additional features such as using word2vec and doc2vec word embedding.
- Experiment with different n-gram values and compare the performance.
- Gather data from other online sources aside from Twitter.

## License
This project is licensed under the MIT License.