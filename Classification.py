import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier


dataset = pd.read_csv('combined_data.csv', delimiter=',', encoding='latin-1')

labels = (dataset[['won']]).values.tolist()
inputs = dataset.drop(columns=['Unnamed: 0', 'won'])
labels = np.array(labels).squeeze()

train_inputs, test_inputs, train_labels, test_labels = train_test_split(inputs, labels, test_size=0.2)

model = RandomForestClassifier().fit(train_inputs, train_labels)
predictions = model.predict(test_inputs)

print(1- np.sum(np.abs((predictions-test_labels)) / len(test_labels)))
cm = confusion_matrix(test_labels, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Did not win', 'Win'])
disp.plot()
plt.title('Model Predicting If Horse Wins')
plt.show()
