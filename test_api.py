import requests
import json

API_URL = 'http://127.0.0.1:5000/evaluate'

test_data = {
  'LIMIT_BAL': 500000, 
  'SEX': 1, 
  'EDUCATION': 1, 
  'MARRIAGE': 1, 
  'AGE': 25, 
  'PAY_1': 2, # Two months behind on payment
  'PAY_2': 2, 
  'PAY_3': 2, 
  'PAY_4': 2, 
  'PAY_5': 2, 
  'PAY_6': 2, 
  'BILL_AMT1': 400000, 
  'BILL_AMT2': 380000, 
  'BILL_AMT3': 360000, 
  'BILL_AMT4': 340000, 
  'BILL_AMT5': 320000, 
  'BILL_AMT6': 300000, 
  'PAY_AMT1': 0, 
  'PAY_AMT2': 0, 
  'PAY_AMT3': 0, 
  'PAY_AMT4': 0, 
  'PAY_AMT5': 0, 
  'PAY_AMT6': 0
}

headers = {'Content-Type': 'application/json'}

try:
  # json.dumps used to convert python dict data to JSON
  response = requests.post(API_URL, headers=headers, data=json.dumps(test_data))

  if response.status_code == 200:
    print("\n API Response Received")
    # Converts json back to Python dict format with indent for readability
    print(json.dumps(response.json(), indent=4))
  else:
    print(f"\n API Error")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

except requests.exceptions.ConnectionError:
  print("\nError: COuld not connect tot he API. Please check api.py is still \
  running ")