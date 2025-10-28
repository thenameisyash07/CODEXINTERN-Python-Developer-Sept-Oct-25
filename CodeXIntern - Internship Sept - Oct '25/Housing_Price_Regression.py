# housing_price_regression_basic.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('housing.csv')
print(f"Loaded dataset with shape: {df.shape}")


target = 'median_house_value'

# Separate features and target
X = df.drop(columns=[target])
y = df[target]


X = pd.get_dummies(X, drop_first=True)


X = X.dropna()
y = y.loc[X.index]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Metrics
rmse = mean_squared_error(y_test, preds, squared=False)
r2 = r2_score(y_test, preds)

print(f"RMSE: {rmse:.2f}")
print(f"R^2: {r2:.4f}")
