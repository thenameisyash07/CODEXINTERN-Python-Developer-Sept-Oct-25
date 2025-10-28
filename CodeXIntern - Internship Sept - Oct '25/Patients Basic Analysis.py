import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("patients.csv")

# Basic Data Analysis
print("First 5 rows:")
print(df.head())

print("Average age:", df["age"].mean())
print("Average satisfaction:", df["satisfaction"].mean())
print("Total patients:", len(df))

# Patients per service
service_counts = df["service"].value_counts()
print("Patients per service:")
print(service_counts)

# Bar Chart — Service vs Count
service_counts.plot(kind="bar")
plt.title("Patients Per Service")
plt.xlabel("Service")
plt.ylabel("Count")
plt.show()

# Scatter Plot — Age vs Satisfaction
plt.scatter(df["age"], df["satisfaction"])
plt.title("Age vs Satisfaction")
plt.xlabel("Age")
plt.ylabel("Satisfaction")
plt.show()

# Heatmap — Correlation Between Numeric Columns
corr = df.corr(numeric_only=True)
plt.imshow(corr, cmap="viridis")
plt.title("Correlation Heatmap")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.show()
