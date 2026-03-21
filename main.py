import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# sample data
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [20000, 25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

X = df[["experience"]]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

print("Prediction for 6 years experience:", model.predict([[6]]))