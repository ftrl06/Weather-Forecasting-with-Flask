from flask import render_template, request, jsonify
from app import app
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('../model/model.pkl')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction[0]})
