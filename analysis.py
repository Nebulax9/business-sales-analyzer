def calculate_overall_metrics(sales_data):

    # Total Revenue
    total_revenue = sales_data["Revenue"].sum()

    # Total Cost
    total_cost = sales_data["Cost"].sum()

    # Total Profit
    total_profit = total_revenue - total_cost

    # Total Quantity Sold
    total_quantity = sales_data["Quantity"].sum()

    # Overall Profit Margin
    overall_profit_margin = (total_profit / total_revenue) * 100

    results = {
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_profit": total_profit,
        "total_quantity": total_quantity,
        "overall_profit_margin": overall_profit_margin
    }

    return results


def analyze_products(sales_data):

    # Revenue by Product
    revenue_by_product = sales_data.groupby("Product")["Revenue"].sum()

    # Cost by Product
    cost_by_product = sales_data.groupby("Product")["Cost"].sum()

    # Profit by Product
    profit_by_product = revenue_by_product - cost_by_product

    # Profit Margin by Product
    profit_margin_by_product = ((profit_by_product / revenue_by_product) * 100).round(2)

    # Quantity by Product
    quantity_by_product = sales_data.groupby("Product")["Quantity"].sum()

    # Highest-Revenue Product
    highest_revenue_product = revenue_by_product.idxmax()
    highest_product_revenue = revenue_by_product.max()

    # Highest Profit-Margin Product
    highest_margin_product = profit_margin_by_product.idxmax()
    highest_profit_margin = profit_margin_by_product.max()

    # Highest-Profit Product
    highest_profit_product = profit_by_product.idxmax()
    highest_product_profit = profit_by_product.max()

    # Most-Sold Product
    most_sold_product = quantity_by_product.idxmax()
    most_sold_quantity = quantity_by_product.max()

    # Highest Individual Revenue Transaction
    highest_transaction_index = sales_data["Revenue"].idxmax()
    highest_transaction_revenue = sales_data["Revenue"].max()
    highest_transaction_product = sales_data.loc[highest_transaction_index, "Product"]

    results = {
        "revenue_by_product": revenue_by_product,
        "cost_by_product": cost_by_product,
        "profit_by_product": profit_by_product,
        "profit_margin_by_product": profit_margin_by_product,
        "quantity_by_product": quantity_by_product,
        "highest_revenue_product": highest_revenue_product,
        "highest_product_revenue": highest_product_revenue,
        "highest_margin_product": highest_margin_product,
        "highest_profit_margin": highest_profit_margin,
        "highest_profit_product": highest_profit_product,
        "highest_product_profit": highest_product_profit,
        "most_sold_product": most_sold_product,
        "most_sold_quantity": most_sold_quantity,
        "highest_transaction_product": highest_transaction_product,
        "highest_transaction_revenue": highest_transaction_revenue
    }

    return results


def analyze_regions(sales_data):

    # Revenue by Region
    revenue_by_region = sales_data.groupby("Region")["Revenue"].sum()

    # Cost by Region
    cost_by_region = sales_data.groupby("Region")["Cost"].sum()

    # Profit by Region
    profit_by_region = revenue_by_region - cost_by_region

    # Profit Margin by Region
    profit_margin_by_region = (profit_by_region / revenue_by_region) * 100

    # Highest-Revenue Region
    highest_revenue_region = revenue_by_region.idxmax()
    highest_region_revenue = revenue_by_region.max()

    results = {
        "revenue_by_region": revenue_by_region,
        "cost_by_region": cost_by_region,
        "profit_by_region": profit_by_region,
        "profit_margin_by_region": profit_margin_by_region,
        "highest_revenue_region": highest_revenue_region,
        "highest_region_revenue": highest_region_revenue
    }

    return results


def analyze_months(sales_data):

    # Create a Month Column
    sales_data["Month"] = sales_data["Date"].dt.to_period("M")

    # Revenue by Month
    revenue_by_month = sales_data.groupby("Month")["Revenue"].sum()

    # Cost by Month
    cost_by_month = sales_data.groupby("Month")["Cost"].sum()

    # Profit by Month
    profit_by_month = revenue_by_month - cost_by_month

    # Profit Margin by Month
    profit_margin_by_month = (profit_by_month / revenue_by_month) * 100

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

    # Quantity by Product by Month
    quantity_by_product_by_month = sales_data.groupby(["Month", "Product"])["Quantity"].sum()

    results = {
        "revenue_by_month": revenue_by_month,
        "cost_by_month": cost_by_month,
        "profit_by_month": profit_by_month,
        "profit_margin_by_month": profit_margin_by_month,
        "revenue_growth": revenue_growth,
        "quantity_by_product_by_month": quantity_by_product_by_month
    }

    return results