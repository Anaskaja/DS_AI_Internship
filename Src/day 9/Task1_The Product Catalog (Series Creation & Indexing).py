import pandas as pd

Products=pd.Series([700,670,780,800],index=['Laptop','monitor','cpu','projector'])
laptop_price=Products['Laptop']
print(Products)
print(laptop_price)
first_two_products =Products[:2]
print(first_two_products)