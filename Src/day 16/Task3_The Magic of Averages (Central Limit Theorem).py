import numpy as np
import matplotlib.pyplot as plt

print("--- Task 3: The Magic of Averages ---")

# --- 1. Heavily Skewed Dataset ---
# Creating a right-skewed dataset (like income)
population = np.random.exponential(scale=50000, size=10000)

# --- 2. Run a loop 1,000 times ---
# Take a random sample of 30 values and calculate the mean
sample_means = []
for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())

# --- 3. Plot a histogram of those 1,000 means ---
#
plt.figure(figsize=(8, 5))
plt.hist(sample_means, bins=30, color='purple', edgecolor='black')
plt.title("Distribution of 1,000 Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()

# --- 4. Required Observation ---
#
print("\nObservation: Even if the original data was ugly and skewed, the distribution of the means will look like a beautiful bell curve.")