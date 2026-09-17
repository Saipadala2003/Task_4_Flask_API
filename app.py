from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load trained model
try:
    model = tf.keras.models.load_model("deep_learning_model.h5")
    print("Model loaded successfully!")
except Exception as e:
    model = None
    print("Error loading model:", str(e))


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Deep Learning Model API is running",
        "status": "success"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Check JSON
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "Request must contain JSON data"
            }), 400

        data = request.get_json()

        # Check input_data
        if "input_data" not in data:
            return jsonify({
                "status": "error",
                "message": "Missing 'input_data' field"
            }), 400

        input_data = data["input_data"]

        # Convert input to NumPy array
        input_array = np.array(input_data, dtype=np.float32)

        # Check input shape
        if input_array.size != 784:
            return jsonify({
                "status": "error",
                "message": "input_data must contain exactly 784 pixel values"
            }), 400

        # Reshape image to 28x28
        input_array = input_array.reshape(1, 28, 28, 1)

        # Normalize pixels
        input_array = input_array / 255.0

        # Make prediction
        prediction = model.predict(input_array)

        # Find predicted digit
        predicted_digit = int(np.argmax(prediction[0]))

        # Confidence
        confidence = float(np.max(prediction[0]))

        return jsonify({
            "status": "success",
            "predicted_digit": predicted_digit,
            "confidence": confidence
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
