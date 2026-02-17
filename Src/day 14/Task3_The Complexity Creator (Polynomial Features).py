import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

print("--- Task 3: The Complexity Creator ---")


X = np.sort(np.random.rand(20, 1) * 10, axis=0)
y = (0.5 * X**2 + X + 2 + np.random.randn(20, 1)).flatten() # y = x^2 (Curved)

#Train Linear Regression
model_linear = LinearRegression()
model_linear.fit(X, y)
r2_linear = r2_score(y, model_linear.predict(X))

# Create Polynomial Features (Degree=2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

#Train Linear Regression on Polynomial Features
model_poly = LinearRegression()
model_poly.fit(X_poly, y)
r2_poly = r2_score(y, model_poly.predict(X_poly))

# Documented R2 score for both
print(f"R² Score (Original Linear): {r2_linear:.4f}")
print(f"R² Score (Polynomial Deg=2): {r2_poly:.4f}")

print("\nObservation: Yes, the curved features helped significantly. The Polynomial model has a much higher R² score because it can fit the non-linear curve.")

