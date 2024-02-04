import pandas as pd

#Read in both data
races_data = pd.read_csv('new_races_data.csv', delimiter=',', encoding='latin-1')
runs_data = pd.read_csv('new_runs_data.csv', delimiter=',', encoding='latin-1')

#Add races d
races_columns = list(races_data.columns)[2:]
new_columns = list(runs_data.columns)[1:] + races_columns
runs_data = runs_data.reindex(columns=new_columns, fill_value=0)

for index, row in runs_data.iterrows():
    for col_name in races_columns:
        id = int(pd.Series(row['race_id']).loc[0])
        race = races_data.loc[races_data['race_id'] == id]
        runs_data.at[index, col_name] = int(race[col_name].iloc[0])


runs_data.to_csv('combined_data.csv')