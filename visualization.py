import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

invoice = pd.read_csv("c:/Users/Admin/Desktop/InvoicePurchases12312016.csv")

top_vendors = invoice.groupby("VendorName")["Dollars"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_vendors.index, y=top_vendors.values)
plt.title("Top 10 Vendors by Purchase Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
