import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#dataset
data = {
    'Price': [300000, 450000, 350000, 400000, 320000, 2500000, 380000, 420000, 2800000],
    'SquareFootage': [1500, 2000, 1600, 2200, 1550, 4500, 1800, 2100, 5000],
    'Bedrooms': [2, 3, 2, 3, 2, 5, 3, 3, 5]
}
df = pd.DataFrame(data)

# CORRELATION MATRIX & HEATMAP 

plt.figure(figsize=(8, 6))
corr_matrix = df.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

#boxplot, outlier detection
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Price'])
plt.title("Outlier Detection in Price")
plt.xlabel("Price (INR)")
plt.show()
print("1. High Correlation (>0.8): 'Price' and 'SquareFootage' are highly correlated (Close to 1.0).")
print("2. Outliers Identified: The Boxplot shows distinct points on the far right (Price > 2,000,000).")
