import pandas as pd
import numpy as np

print("--- Task 2: The Outlier Detective ---")

# --- 1. Create Dataset ---
# A simple dataset where most values are normal, but '100' is an extreme outlier.
df = pd.DataFrame({'Value': [10, 12, 11, 10, 13, 12, 11, 14, 10, 100]})

# --- 2. Calculate Mean (μ) and Standard Deviation (σ) ---
#
mu = df['Value'].mean()
sigma = df['Value'].std()

print(f"Mean (μ): {mu:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}\n")

# --- 3. Create z_score column ---
# Formula: Z = (x - μ) / σ
df['z_score'] = (df['Value'] - mu) / sigma

print("Full Dataset with Z-Scores:")
print(df)

# --- 4. Identify Outliers (|Z| > 3) ---
#
outliers = df[np.abs(df['z_score']) > 3]

print("\n--- Identified Outliers (|Z| > 3) ---")
print(outliers)