import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#dataset
data = {
    'Price': [300000, 450000, 350000, 400000, 320000, 2500000, 380000, 420000, 2800000],
    'SquareFootage': [1500, 2000, 1600, 2200, 1550, 4500, 1800, 2100, 5000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
}
df = pd.DataFrame(data)

#scatterplot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title("Relationship: House Size vs. Price")
plt.xlabel("Square Footage (sq ft)")
plt.ylabel("Price (INR)")
plt.grid(True)
plt.show()

# Boxplot 
plt.figure(figsize=(8, 5))
sns.boxplot(x='City', y='Price', data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price (INR)")
plt.show()

# --- REQUIRED OBSERVATION ---
print("\nObservation: As Square Footage increases, the Price seems to INCREASE significantly.")