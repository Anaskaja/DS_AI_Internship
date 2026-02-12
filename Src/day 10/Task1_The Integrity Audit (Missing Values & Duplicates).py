import pandas as pd
print("---The Integrity Audit---")
df=pd.read_csv('customer_orders.csv')

print(f"Original Data Shape: {df.shape}")
print(df)

print('\n---Missing values of the data---')
print(df.isna().sum())
median_val =df['Amount'].median()
df['Amount']=df['Amount'].fillna(median_val)

print('Filled missing values _median:',median_val)
print('Filled amount:',df['Amount'])

df_clean = df.drop_duplicates()

print(f"Final Cleaned Data Shape:{df_clean.shape}")
print(df_clean)