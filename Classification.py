import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier

#read in data
dataset = pd.read_csv('data/combined_data.csv', delimiter=',', encoding='latin-1')

#separate into inputs and outputs, remove results from inputs
labels = (dataset[['won']]).values.tolist()
inputs = dataset.drop(columns=['Unnamed: 0', 'won', 'place_combination1', 'place_combination2'])
labels = np.array(labels).squeeze()

#split into 80-20 train test
train_inputs, test_inputs, train_labels, test_labels = train_test_split(inputs, labels, test_size=0.2)

#create, train, and predict using model
model = RandomForestClassifier().fit(train_inputs, train_labels)
predictions = model.predict(test_inputs)

#show results using confusion matrix
cm = confusion_matrix(test_labels, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Did not win', 'Win'])
disp.plot()
plt.title('Model Predicting If Horse Wins')
plt.show()

#show feature importance
importance = model.feature_importances_
print(importance)
print(inputs.columns) 

#Accuracy, performance metric
print("Accuracy: " + str(1- np.sum(np.abs((predictions-test_labels)) / len(test_labels))))