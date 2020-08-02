import pandas as pd

Military_Expenditure = pd.read_csv("data.csv")

Military_Expenditure.drop(['Indicator Name'], axis='columns', inplace=True)

Military_Expenditure= Military_Expenditure.melt(id_vars=['Name', 'Code', 'Type'],
                                         var_name='Year', value_name='Expenditure_USD')

Military_Expenditure[["Year"]] = Military_Expenditure[["Year"]].astype("int")

Military_Expenditure.fillna(value=0, inplace=True)

Military_Expenditure.to_csv('data_cleaned.csv')

print(Military_Expenditure.head())