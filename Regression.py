import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

#Read in dataset
dataset = pd.read_csv('data/combined_data.csv', delimiter=',', encoding='latin-1')

#For winners only
dataset = dataset.loc[dataset['won'] == 1]

#Show correlations - not much except distance and final_time (which means very predictive)
    #Too many numbers to see well
# correlations = dataset.corr(numeric_only = True)
# sns.clustermap(correlations, cmap='coolwarm', annot=True)
# plt.show()

#Create inputs and labels
labels = (dataset[['finish_time']]).values.tolist()
inputs = dataset.drop(columns=['Unnamed: 0', 'finish_time'])
labels = np.array(labels).squeeze()

#Split into train and test with 80-20
train_inputs, test_inputs, train_labels, test_labels = train_test_split(inputs, labels, test_size=0.2)

#Build model, train, and predict
model = RandomForestRegressor(random_state=0).fit(train_inputs, train_labels)
predictions = model.predict(test_inputs)

#Show results using scatter plot
plt.scatter(predictions, test_labels)
plt.title('Model Predicting Horse Finish Time')
plt.xlabel('Predicted Finish Time')
plt.ylabel('Actual Finish Time')
plt.show()

#See relative importance of all feature inputs
importance = model.feature_importances_
print(importance)
print(inputs.columns) 

#Get MSE, evaluation metric
print("MSE:", mean_squared_error(test_labels,predictions))