import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

print("--- Task 2: The Leveling Field (Feature Scaling) ---")

#Data

data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Salary': [30000, 40000, 50000, 60000, 80000, 100000, 120000, 150000]
}
df = pd.DataFrame(data)

# Standard scaler(standarized)
scaler_std = StandardScaler()
df_std = pd.DataFrame(scaler_std.fit_transform(df), columns=['Age', 'Salary'])

# Min max scaler(normalized)

scaler_minmax = MinMaxScaler()
df_minmax = pd.DataFrame(scaler_minmax.fit_transform(df), columns=['Age', 'Salary'])
# Compare Histograms 
plt.figure(figsize=(15, 5))

# Plot 1: Original
plt.subplot(1, 3, 1)
sns.histplot(df['Salary'], kde=True, color='blue')
plt.title("Original Salary\n(Range: 30,000 to 150,000)")
plt.xlabel("Salary (INR)")

# Plot 2: Standard Scaled
plt.subplot(1, 3, 2)
sns.histplot(df_std['Salary'], kde=True, color='red')
plt.title("Standard Scaled\n(Centered at Mean 0)")
plt.xlabel("Standardized Score")

# Plot 3: Min-Max Scaled
plt.subplot(1, 3, 3)
sns.histplot(df_minmax['Salary'], kde=True, color='green')
plt.title("Min-Max Scaled\n(Fixed Range 0 to 1)")
plt.xlabel("Normalized Score")

plt.tight_layout()
plt.show()

