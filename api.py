import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler

MODEL = joblib.load("rf_model.joblib")
SCALER = joblib.load("scaler.joblib")

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
  data = request.get_json(force=True)

  # Conversion of form data to become Pandas DataFrame friendly
  data_df = pd.DataFrame([data])

  FEATURES = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1',
    'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
    'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2',
    'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
    ]

  # Arranges the feature data into the exact order as above.
  input_data = data_df[FEATURES]

  scaled_input_data = SCALER.transform(input_data)

  result = MODEL.predict(scaled_input_data)

  risk_outcome = result.tolist()[0]

  return jsonify({
    'evaluation': risk_outcome,
    'message': 'Model predicts Client will go into arrears.' \
    if risk_outcome == 1 else 'Model predicts Client is low risk.'
  })


if __name__ == '__main__':
  print("Starting Flask application...")
  app.run(debug=True)
