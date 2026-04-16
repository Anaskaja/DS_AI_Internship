import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the AI model we just trained
model = joblib.load('abalone_predictor.joblib')

@app.route('/')
def home():
    return "Day 56: Abalone Age Predictor API is Live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            data.get('length', 0),
            data.get('diameter', 0),
            data.get('height', 0),
            data.get('whole_weight', 0)
        ]
        prediction = model.predict([features])[0]
        return jsonify({'predicted_abalone_age': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)