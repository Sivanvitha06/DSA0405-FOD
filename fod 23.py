# Import necessary libraries
import pandas as pd
# Load your dataset
# Replace 'your_dataset.csv' with the actual file name or provide the appropriate path
df = pd.read_csv('your_dataset.csv')

# Assume 'risk' is the target variable, and 'income', 'credit score', 'debt-to-income ratio', 'employment duration' are features
X = df[['income', 'credit score', 'debt-to-income ratio', 'employment duration']]
y = df['risk']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the CART classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Display classification report for more detailed evaluation
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Predict credit risk level for a new loan applicant
# Replace the values in the new_applicant array with the specific attribute values for the new applicant
new_applicant = [[new_income, new_credit_score, new_debt_to_income, new_employment_duration]]
new_applicant_scaled = scaler.transform(new_applicant)
predicted_risk = clf.predict(new_applicant_scaled)

print(f'Predicted Credit Risk for the New Applicant: {predicted_risk[0]}')
