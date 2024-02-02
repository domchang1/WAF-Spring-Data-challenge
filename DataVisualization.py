import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read in data
races_data = pd.read_csv('races_data.csv', delimiter=',', encoding='latin-1')
runs_data = pd.read_csv('runs.csv', delimiter=',', encoding='latin-1')

#convert each entry to True if null, False otherwise
races_data_null = races_data.isnull()
runs_data_null = runs_data.isnull()
#print(races_data_null.head())

#now plot to visualize which columns are mostly null

# counts = races_data_null.apply(pd.value_counts)
# counts.T.plot(kind='bar', stacked=True)
# plt.show()
# counts = runs_data_null.apply(pd.value_counts)
# counts.T.plot(kind='bar', stacked=True)
# plt.show()

#drop almost completely to completely null columns
races_columns_drop = ['sec_time5','sec_time6','sec_time7',
    'time5', 'time6', 'time7', 'place_combination4', 'place_dividend4',
      'win_combination2', 'win_dividend2']
races_data.drop(columns=races_columns_drop, inplace=True)
runs_columns_drop = ['position_sec5','position_sec6',
    'behind_sec5', 'behind_sec6', 'time5', 'time6']
runs_data.drop(columns=runs_columns_drop, inplace=True)
runs_data_null = runs_data.isnull()
counts = runs_data_null.apply(pd.value_counts)
counts.T.plot(kind='bar', stacked=True)
plt.show()

races_data.drop(columns=['win_combination1', 'win_dividend1'], inplace=True)

runs_data['horse_id'].plot(kind='hist', edgecolor='black')
plt.show()

print(runs_data['horse_age'].std())
print(runs_data['horse_rating'].std())
