import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


races_data = pd.read_csv('races_data.csv', delimiter=',', encoding='latin-1')
runs_data = pd.read_csv('runs.csv', delimiter=',', encoding='latin-1')


races_data_null = races_data.isnull()
runs_data_null = runs_data.isnull()
print(races_data_null.head())

counts = races_data_null.apply(pd.value_counts)
counts.T.plot(kind='bar', stacked=True)
plt.show()

counts = runs_data_null.apply(pd.value_counts)
counts.T.plot(kind='bar', stacked=True)
plt.show()

exit()

#runs_data = runs_data.dropna()

