import pandas as pd

beg = pd.read_csv("C:/Users/Admin/Desktop/BegInvFINAL12312016.csv")
end = pd.read_csv("c:/Users/Admin/Desktop/EndInvFINAL12312016.csv")
sales = pd.read_csv("C:/Users/Admin/Desktop/SalesFINAL12312016.csv")

average_inventory = (beg["onHand"].sum() + end["onHand"].sum()) / 2
cost_of_goods_sold = sales["SalesDollars"].sum()

inventory_turnover = cost_of_goods_sold / average_inventory
print("Inventory Turnover:", round(inventory_turnover, 2))


import math

annual_demand = 50000
ordering_cost = 200
holding_cost = 50

EOQ = math.sqrt((2 * annual_demand * ordering_cost) / holding_cost)
print("EOQ:", round(EOQ))

