import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor


dataset = pd.read_csv('new_runs_data.csv', delimiter=',', encoding='latin-1')

labels = (dataset[['finish_time']]).values.tolist()
inputs = dataset.drop(columns=['Unamed: 0', 'finish_time'])
labels = np.array(labels).squeeze()
print(inputs)
print(labels)

# inputs = (inputs-inputs.min())/(inputs.max()-inputs.min()).tolist()

train_inputs, test_inputs, train_labels, test_labels = train_test_split(inputs, labels, test_size=0.2)

model = KNeighborsRegressor().fit(train_inputs, train_labels)
predictions = model.predict(test_inputs)

plt.scatter(predictions, test_labels)
plt.xlabel('Predicted Finish Time')
plt.ylabel('Actual Finish Time')
plt.show()

print("MSE:", mean_squared_error(test_labels,predictions))
