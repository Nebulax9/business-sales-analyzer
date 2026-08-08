import pandas as pd


# Load the Excel Sales Data
sales_data = pd.read_excel("sample_sales.xlsx")
print(sales_data)


# ------------------------------------------------------------
# 1. Overall Company Metrics
print()
print()

# Basic Business Metrics
total_revenue = sales_data["Revenue"].sum()
total_cost = sales_data["Cost"].sum()
total_profit = total_revenue - total_cost
total_quantity = sales_data["Quantity"].sum()

print(f"The total revenue is: ${total_revenue}")
print(f"The total cost is: ${total_cost}")
print(f"The total profit is: ${total_profit}")
print(f"The total quantity sold is: {total_quantity}")
print()
print()

# Overall Profit Margin
overall_profit_margin = (total_profit / total_revenue) * 100

print(f"The overall profit margin is {overall_profit_margin:.2f}%.")
print()
print()

# ------------------------------------------------------------
# 2. Product Analysis

# Highest-Revenue Product
revenue_by_product = sales_data.groupby("Product")["Revenue"].sum()
highest_revenue_product = revenue_by_product.idxmax()
highest_product_revenue = revenue_by_product.max()

print(f"The company's highest-revenue product is a {highest_revenue_product}, with a total revenue of ${highest_product_revenue}.")
print()
print()
# Highest Profit-Margin Product
cost_by_product = sales_data.groupby("Product")["Cost"].sum()
profit_by_product = revenue_by_product - cost_by_product
profit_margin_by_product = (profit_by_product / revenue_by_product) * 100

highest_margin_product = profit_margin_by_product.idxmax()
highest_profit_margin = profit_margin_by_product.max()

print(f"The product with the highest profit margin is {highest_margin_product}, with a margin of {highest_profit_margin:.2f}%.")
print()
print()
# Highest-Profit Product
highest_profit_product = profit_by_product.idxmax()
highest_product_profit = profit_by_product.max()

print(f"The product with the highest total profit is {highest_profit_product}, with a profit of ${highest_product_profit}.")
print()
print()
# Most-Sold Product
quantity_by_product = sales_data.groupby("Product")["Quantity"].sum()
most_sold_product = quantity_by_product.idxmax()
most_sold_quantity = quantity_by_product.max()

print(f"The most-sold product is {most_sold_product}, with {most_sold_quantity} units sold.")
print()
print()
# Highest Individual Revenue Transaction
highest_transaction_index = sales_data["Revenue"].idxmax()
highest_transaction_revenue = sales_data["Revenue"].max()
highest_transaction_product = sales_data.loc[highest_transaction_index, "Product"]

print(f"The highest individual revenue transaction was for a {highest_transaction_product}, with revenue of ${highest_transaction_revenue}.")
print()
print()

# ------------------------------------------------------------
# 3. Region Analysis

# Highest-Revenue Region
revenue_by_region = sales_data.groupby("Region")["Revenue"].sum()
highest_revenue_region = revenue_by_region.idxmax()
highest_region_revenue = revenue_by_region.max()

print(f"The highest-revenue region is {highest_revenue_region}, with total revenue of ${highest_region_revenue}.")
print()
print()
# Profit by Region
cost_by_region = sales_data.groupby("Region")["Cost"].sum()
profit_by_region = revenue_by_region - cost_by_region

print(f"The profit by region is:\n{profit_by_region}")
print()
print()
# Profit Margin by Region
profit_margin_by_region = (profit_by_region / revenue_by_region) * 100

print(f"The profit margin by region is:\n{profit_margin_by_region.round(2)}")
print()
print()

# ------------------------------------------------------------
# 4. Monthly / Time Analysis

# Create a Month Column
sales_data["Month"] = sales_data["Date"].dt.to_period("M")

# Revenue by Month
revenue_by_month = sales_data.groupby("Month")["Revenue"].sum()

print(f"The revenue by month is:\n{revenue_by_month}")
print()
print()
# Profit by Month
cost_by_month = sales_data.groupby("Month")["Cost"].sum()
profit_by_month = revenue_by_month - cost_by_month

print(f"The profit by month is:\n{profit_by_month}")
print()
print()
# Profit Margin by Month
profit_margin_by_month = (profit_by_month / revenue_by_month) * 100

print(f"The profit margin by month is:\n{profit_margin_by_month.round(2)}")
print()
print()
# Revenue Growth by Month
revenue_growth = {}
months = list(revenue_by_month.index)

for i in range(1, len(months)):
    current_month = months[i]
    previous_month = months[i - 1]

    current_revenue = revenue_by_month[current_month]
    previous_revenue = revenue_by_month[previous_month]

    growth = ((current_revenue - previous_revenue) / previous_revenue) * 100

    revenue_growth[current_month] = growth
    print(revenue_growth)


# ------------------------------------------------------------
# 5. Product Over Time
print()
print()
# Quantity by Product by Month
quantity_by_product_by_month = sales_data.groupby(["Month", "Product"])["Quantity"].sum()

print(f"The quantity sold by product each month is: {quantity_by_product_by_month}")