import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("--- Task 1: The Categorical Converter (Encoding) ---")


# Data
data = {
    'Car_ID': [1, 2, 3, 4, 5],
    'Transmission': ['Automatic', 'Manual', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}
df = pd.DataFrame(data)
print(df.info())

# LABEL ENCODING
le = LabelEncoder()
df['Transmission_Encoded'] = le.fit_transform(df['Transmission'])

# ONE-HOT ENCODING

df_final = pd.get_dummies(df, columns=['Color'], drop_first=True, dtype=int)



print(df_final)