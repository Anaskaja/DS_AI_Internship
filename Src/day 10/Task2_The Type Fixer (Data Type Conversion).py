import pandas as pd

print('--The Type Fixer--')

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Price': ['$1200.50', '$25.00', '$300.00', '$45.99']  # Price has '$' symbol
}
df = pd.DataFrame(data)

print("Original data types:-")
print(df.dtypes)

df['Price'] = df['Price'].str.replace('$', '')
df['Price'] = df['Price'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])

print("Fixed data types")
print(df.dtypes)
