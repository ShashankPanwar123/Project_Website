from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    age = int(data["age"])
    premium = float(data["premium"])
    vehicle_age = int(data["vehicle_age"])

    input_data = np.array([[age, premium, vehicle_age]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    return jsonify({
        "prediction": int(prediction),
        "probability": round(probability, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)