import pandas as pd

sales = pd.read_csv("C:/Users/Admin/Desktop/SalesFINAL12312016.csv")

# Basic statistics
print(sales.describe())

# Top selling products
top_products = sales.groupby("Description")["SalesQuantity"].sum().sort_values(ascending=False).head(10)

print(top_products)
