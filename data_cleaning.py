import pandas as pd

purchase_price = pd.read_csv("C:/Users/Admin/Desktop/2017PurchasePricesDec.csv")

# Check null values
print(purchase_price.isnull().sum())

# Drop missing rows
purchase_price.dropna(inplace=True)

# Data types
print(purchase_price.dtypes)

print("Cleaning Completed")
