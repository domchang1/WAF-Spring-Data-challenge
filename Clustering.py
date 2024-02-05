import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#UNFINISHED#

#read in data
dataset = pd.read_csv('data/combined_data.csv', delimiter=',', encoding='latin-1')
dataset = dataset.drop(columns=['Unnamed: 0'])

#Create/train clustering model
model = KMeans(n_clusters=5).fit(dataset)

# Get cluster labels and evaluate with silhouette score
labels = model.labels_  
silhouette_avg = silhouette_score(dataset, labels)
print(f"Silhouette Score: {silhouette_avg}")
