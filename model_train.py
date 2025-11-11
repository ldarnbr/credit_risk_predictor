import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from data_prep import load_data
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

df = load_data()

# Features: containing the information for prediction
# axis=1 tells pandas to consider these as columns not rows.
# ID is not a feature that predicts credit defaults.
X = df.drop(['DEFAULTED', 'ID'], axis = 1)

# Target: the single column we're trying to predict
y = df['DEFAULTED']

# Utilises 80% of the data for training (24k rows), 20% for testing (6k rows)
X_train, X_test, y_train, y_test = train_test_split(
  X, y,
  test_size = 0.2,
  random_state = 42
)

# Data is scaled to make all integers contribute equally to the model
# Example: Age range 20 - 80 vs Credit 10,0000 to 8000,000. 
# relatively small changes in credit ~20,000 are considered massively
# more important than the largest changes in age due to scale.
scaler = StandardScaler()

# Calculates the mean and STD fromt he training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data using the mean/STD from the training data
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(
  random_state = 42,
  n_estimators = 200,
  class_weight = 'balanced'
)

# Model trained from the training features (X_train) and their outcomes (y_train)
model.fit(X_train_scaled, y_train)

y_prediction = model.predict(X_test_scaled)

# Model Evaluation ------------------------------------------------------------

cm = confusion_matrix(y_test, y_prediction)
print("\n Confusion Matrix:")
print(cm)

report = classification_report(y_test, y_prediction)
print("\n Classification Report")
print(report)

print("\n Model Trained and Evaluated.")
