import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

print("Downloading dataset...")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
columns = ['sex', 'length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings']
df = pd.read_csv(url, names=columns)

print("Training model...")
X = df[['length', 'diameter', 'height', 'whole_weight']]
y = df['rings']

model = RandomForestRegressor(n_estimators=100, random_state=123)
model.fit(X, y)

print("Saving model...")
joblib.dump(model, 'abalone_predictor.joblib')
print("Done! The model is saved.")
