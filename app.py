import pandas as pd


# Load the Excel sales data
sales_data = pd.read_excel("sample_sales.xlsx")
print(sales_data)


# Basic Business Metrics
total_revenue = sales_data["Revenue"].sum()
total_cost = sales_data["Cost"].sum()
total_profit = total_revenue - total_cost
total_quantity = sales_data["Quantity"].sum()

print(f"The total revenue is: ${total_revenue}")
print(f"The total cost is: ${total_cost}")
print(f"The total profit is: ${total_profit}")
print(f"The total quantity sold is: {total_quantity}")


# Highest-Revenue Product
revenue_by_product = sales_data.groupby("Product")["Revenue"].sum()
highest_revenue_product = revenue_by_product.idxmax()
highest_product_revenue = revenue_by_product.max()

print(f"The company's highest-revenue product is a {highest_revenue_product}, with a total revenue of ${highest_product_revenue}.")


# Highest Individual Revenue Transaction
highest_transaction_index = sales_data["Revenue"].idxmax()
highest_transaction_revenue = sales_data["Revenue"].max()
highest_transaction_product = sales_data.loc[highest_transaction_index, "Product"]

print(f"The highest individual revenue transaction was for a {highest_transaction_product}, with revenue of ${highest_transaction_revenue}.")


# Highest-Revenue Region
revenue_by_region = sales_data.groupby("Region")["Revenue"].sum()
highest_revenue_region = revenue_by_region.idxmax()
highest_region_revenue = revenue_by_region.max()

print(f"The highest-revenue region is {highest_revenue_region}, with total revenue of ${highest_region_revenue}.")

# Highest Profit-Margin Product
cost_by_product = sales_data.groupby("Product")["Cost"].sum()
profit_by_product = revenue_by_product - cost_by_product
profit_margin_by_product = (profit_by_product / revenue_by_product) * 100

highest_margin_product = profit_margin_by_product.idxmax()
highest_profit_margin = profit_margin_by_product.max()

print(f"The product with the highest profit margin is {highest_margin_product}, with a margin of {highest_profit_margin:.2f}%.")

# Highest Profit Product
highest_profit_product = profit_by_product.idxmax()
highest_product_profit = profit_by_product.max()

print(f"The product with the highest total profit is {highest_profit_product}, with a profit of ${highest_product_profit}.")

# Most-Sold Product
quantity_by_product = sales_data.groupby("Product")["Quantity"].sum()
most_sold_product = quantity_by_product.idxmax()
most_sold_quantity = quantity_by_product.max()

print(f"The most-sold product is {most_sold_product}, with {most_sold_quantity} units sold.")

# Overall Profit Margin
overall_profit_margin = (total_profit / total_revenue) * 100

print(f"The overall profit margin is {overall_profit_margin:.2f}%.")