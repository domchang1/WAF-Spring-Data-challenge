import pandas as pd
import numpy as np

races_data = pd.read_csv('new_races_data.csv', delimiter=',', encoding='latin-1')
runs_data = pd.read_csv('new_runs_data.csv', delimiter=',', encoding='latin-1')

races_columns = list(races_data.columns)[2:]
new_columns = list(runs_data.columns)[1:] + races_columns
runs_data = runs_data.reindex(columns=new_columns, fill_value=0)

for index, row in runs_data.iterrows():
    for col_name in races_columns:
        print("index: " + str(index))
        print("column: " + str(col_name))
        print(row)
        print(row['race_id'])
        id = int(pd.Series(row['race_id']).loc['Name'])
        race = races_data.loc[races_data['race_id'] == id]
        print(race)
        exit()
        runs_data.at[index, col_name] = race[0]
        #runs_data.set_value(index, col_name, race)
   

print(runs_data)

