import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Task 1: The Shape Shifter ---")

# Generate Numerical Dataset

np.random.seed(42)
df = pd.DataFrame({
    'Heights_Normal': np.random.normal(loc=170, scale=10, size=1000),
    'Incomes_RightSkew': np.random.exponential(scale=50000, size=1000),
    'Scores_LeftSkew': 100 - np.random.exponential(scale=10, size=1000)
})

#  Plot Histogram with KDE Overlay

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
colors = ['blue', 'green', 'red']

for i, col in enumerate(df.columns):
    sns.histplot(df[col], kde=True, ax=axes[i], color=colors[i])
    
    # Compare Mean and Median
    #
    mean_val = df[col].mean()
    median_val = df[col].median()
    
    axes[i].axvline(mean_val, color='black', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.1f}')
    axes[i].axvline(median_val, color='yellow', linestyle='-', linewidth=2, label=f'Median: {median_val:.1f}')
    axes[i].set_title(col)
    axes[i].legend()

plt.tight_layout()
plt.show()

# --- Required Observation ---

print("\nObservation:")
print("1. Heights_Normal: Mean and Median are roughly equal.")
print("2. Incomes_RightSkew: Mean > Median. (The long right tail pulls the mean higher).")
print("3. Scores_LeftSkew: Mean < Median. (The long left tail pulls the mean lower).")