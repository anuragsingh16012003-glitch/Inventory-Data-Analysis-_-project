import pandas as pd

# Load datasets
purchase_price = pd.read_csv("C:/Users/Admin/Desktop/2017PurchasePricesDec.csv")
begin_inventory = pd.read_csv("C:/Users/Admin/Desktop/BegInvFINAL12312016.csv")
end_inventory = pd.read_csv("c:/Users/Admin/Desktop/EndInvFINAL12312016.csv")
invoice = pd.read_csv("c:/Users/Admin/Desktop/InvoicePurchases12312016.csv")
sales = pd.read_csv("C:/Users/Admin/Desktop/SalesFINAL12312016.csv")

print("Data Loaded Successfully!")
print(purchase_price.head())
