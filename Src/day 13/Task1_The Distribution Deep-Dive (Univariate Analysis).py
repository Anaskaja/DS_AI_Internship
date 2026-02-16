import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset

data = {
    'Price': [300000, 450000, 350000, 400000, 320000, 2500000, 380000, 420000, 2800000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
}
df = pd.DataFrame(data)

#histogram with kde

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True,)
plt.title("Distribution of Housing Prices (Numerical)")
plt.xlabel("Price in INR")
plt.grid(True, alpha=0.3)
plt.show()


#skewness and kurtosis

skew_val = df['Price'].skew()
kurt_val = df['Price'].kurt()

print(f"Skewness: {skew_val:.2f}")
print(f"Kurtosis: {kurt_val:.2f}")

#countplot

plt.figure(figsize=(6, 4))
sns.countplot(x='City', data=df)
plt.title("Property Count by City (Categorical)")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()