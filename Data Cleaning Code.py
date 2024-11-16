import pandas as pd
import numpy as np
import re

df = pd.read_csv('Data.csv')
df.head()

def clean_column_to_numeric(column):
    cleaned_column = column.apply(lambda x: re.sub(r'[^0-9.]', '', str(x)).strip() if pd.notnull(x) else x)
    return pd.to_numeric(cleaned_column, errors='coerce')

# Apply cleaning to each column
columns_to_clean = ['X2', 'X5', 'X6', 'X7', 'X12', 'X13', 'Y (output)']
for column in columns_to_clean:
    df[column] = clean_column_to_numeric(df[column])

# Fill missing values with the median of each column
for column in columns_to_clean:
    df[column].fillna(df[column].median(), inplace=True)

# Drop any duplicate rows
df = df.drop_duplicates()

# Verify the data is clean
missing_values = df.isnull().sum()
data_types = df.dtypes

print("Missing values after cleaning:\n", missing_values)
print("Data types:\n", data_types)

df.to_csv("D:/ACADEMIC DATA/3rd Year(1st sem)/ML Project Theory/Markandey_Vatsa(22bce7577)_Clean_dataset.csv", index=False)








