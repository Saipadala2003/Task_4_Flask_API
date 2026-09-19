# Task 5 - API Testing and Validation using Postman

## Objective
Validate the Flask-based MNIST deep-learning prediction API using Postman.

## System Under Test
The Task 4 Flask implementation exposes:
- GET / — API health check
- POST /predict — MNIST prediction using 784 pixel values

## Test Cases
| ID | Test Case | Request | Expected HTTP |
|---|---|---|---|
| TC-01 | API Health Check | GET / | 200 |
| TC-02 | Valid Prediction | POST /predict | 200 |
| TC-03 | Missing Input Data | POST /predict | 400 |
| TC-04 | Incorrect Pixel Count | POST /predict | 400 |

## Automated Assertions
- API health check: 3 assertions
- Valid prediction: 4 assertions
- Missing input data: 3 assertions
- Incorrect pixel count: 3 assertions
- Total: 13 assertions

## How to Run
1. Start the Flask API from the Task 4 project:
   `python app.py`
2. Confirm the server is running at `http://127.0.0.1:5000`.
3. Import `Postman_Collection.json` into Postman.
4. Run the collection.
5. Open the Postman Collection Runner results and capture screenshots.
6. Save the screenshots in the `screenshots/` folder.

## Expected Error Responses
Missing input_data:
```json
{"message":"Missing 'input_data' field","status":"error"}
```

Incorrect pixel count:
```json
{"message":"input_data must contain exactly 784 pixel values","status":"error"}
```

## Expected Overall Result
13/13 assertions passed and 0 errors when the Flask API is running correctly.

## Project Structure
```
Task_5_API_Testing/
├── Postman_Collection.json
├── README.md
├── screenshots/
└── test_results/
```

## Note
The collection generates a valid 784-value MNIST-shaped input for the prediction test. The test validates that the returned digit is 0-9 and confidence is between 0 and 1; the exact predicted digit depends on the input supplied to the running model.
