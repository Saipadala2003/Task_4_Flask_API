# Task_4_Flask_API
Flask REST API for MNIST Handwritten Digit Classification using a CNN

# Task 4 – Flask API for Deep Learning Models

## MNIST Handwritten Digit Classification

This project demonstrates the deployment of a trained Convolutional Neural Network (CNN)
for MNIST handwritten digit classification using a Flask REST API.

## Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- MNIST Dataset

## Model

The CNN model contains convolutional layers, max-pooling,
a flattening layer, a dense layer, and a 10-class softmax output layer.

The trained model is saved as:

deep_learning_model.h5

## API Endpoints

### GET /

Checks whether the Flask API is running.

### POST /predict

Accepts 784 pixel values representing a 28 × 28 MNIST image.

Example request:

{
  "input_data": [784 pixel values]
}

Example response:

{
  "status": "success",
  "predicted_digit": 7,
  "confidence": 0.999976396560669
}

## Results

The CNN achieved approximately 98.97% test accuracy.

The Flask API successfully predicted an MNIST test image of digit 7
with approximately 99.9976% confidence.

## How to Run

Install dependencies:

pip install flask tensorflow numpy

Run the Flask application:

python app.py

The API will run on:

http://127.0.0.1:5000/
