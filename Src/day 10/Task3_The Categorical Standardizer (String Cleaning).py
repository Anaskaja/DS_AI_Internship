import pandas as pd

print("The Categorical Standardizer")

data = {
    'ID': [101, 102, 103, 104, 105],
    'Location': [' New York', 'new york', 'NEW YORK ', ' Los Angeles', 'los angeles']
}
df = pd.DataFrame(data)

print("Original Unique Locations:")
print(df['Location'].unique())


df['Location'] = df['Location'].str.strip()
df['Location'] = df['Location'].str.title()

print(" Cleaned Unique Locations:")
print(df['Location'].unique())


print("Final Cleaned Data:")
print(df)