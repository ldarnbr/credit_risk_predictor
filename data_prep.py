import pandas as pd

# --- Data sourcing ---
# Title: Default of Credit Card Clients
# Source URL: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
# License: Creative Commons Attribution 4.0 International
# ---------------------

df = pd.read_excel("default of credit card clients.xls", header=1)

# Data numbering currently skips from PAY_0 to PAY_2
df.rename(columns={
    'PAY_0': 'PAY_1',
    'default payment next month': 'DEFAULTED' # Conciseness
}, inplace=True)

print("** DataFrame Head **")
print(df.head())

print("\n** DataFrame Info **")
df.info()

average_age = df['AGE'].mean()

print(f"\nAverage Client Age: {average_age:.2f}")

print("\n** Updated Columns **")
print(df.columns.tolist())