import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ConvertingDataFunctions as CDF

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
# races_data_null = races_data.isnull()
# counts = races_data_null.apply(pd.value_counts)
# counts.T.plot(kind='bar', stacked=True)
# plt.show()

#drop the columns which are redundant/make no sense/trivial/unpredictive
races_data.drop(columns=['date', 'win_combination1', 'win_dividend1'], inplace=True)
runs_data.drop(columns=['result', 'lengths_behind'], inplace=True)
race_drop = ['horse_ratings', 'sec_time1', 'sec_time2', 'sec_time3', 'sec_time4', 'time1','time2', 'time3', 'time4',
    'place_dividend1','place_dividend2','place_dividend3', 'place_combination3']
races_data.drop(columns=race_drop, inplace=True)
runs_drop = ['place_odds', 'position_sec1','position_sec2','position_sec3','position_sec4','behind_sec1',
    'behind_sec2','behind_sec3','behind_sec4','time1','time2','time3','time4']
runs_data.drop(columns=runs_drop, inplace=True)

#print std to test to see how much categories are spread out
# print(runs_data['horse_age'].std())
# print(runs_data['horse_rating'].std())

#convert nonnumerical data to numerical

races_data['venue'] = races_data['venue'].apply(CDF.convert_venue)
#print(races_data['venue'].mean())

#print(races_data['config'].unique())
races_data['config'] = races_data['config'].apply(CDF.convert_config)

#print(races_data['going'].unique())
races_data['going'] = races_data['going'].apply(CDF.convert_going)


# print(runs_data['horse_country'].unique())
# print(runs_data['horse_type'].unique())
runs_data.dropna(subset=['horse_country'], inplace=True)
runs_data['horse_country'] = runs_data['horse_country'].apply(CDF.convert_country)
runs_data['horse_type'] = runs_data['horse_type'].apply(CDF.convert_horse_type)

# print(runs_data['horse_gear'].unique())
runs_data['horse_gear'] = runs_data['horse_gear'].apply(CDF.convert_horse_gear)

races_data['prize'] = races_data['prize'].apply(CDF.convert_prizes)

#Output cleaned data to csvs
races_data.to_csv('new_races_data.csv')
runs_data.to_csv('new_runs_data.csv')
