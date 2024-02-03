import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



dataset = pd.read_csv('races_data.csv', delimiter=',', encoding='latin-1')
# partitioned_dataset = dataset[['DEP_DEL15', 'PRCP', 'SNOW', 'TAVG', 'AWND']]


correlations = dataset.corr(numeric_only = True)
sns.clustermap(correlations, cmap='coolwarm', annot=True)
plt.show()


