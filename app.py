# app.py

from flask import Flask, jsonify, request
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

app = Flask(__name__)

# Load Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train a simple RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# Save the model to a file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']

    # Make predictions using the trained model
    prediction = model.predict([features])[0]

    # Map the numerical prediction back to the corresponding class label
    class_label = iris.target_names[prediction]

    return jsonify({'prediction': class_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

