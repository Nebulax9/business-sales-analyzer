import matplotlib.pyplot as plt
from analysis import analyze_months,analyze_products, analyze_regions
from data_processing import clean_data, load_data
# Monthly Financial Performance

file_source = "sample_sales.xlsx"
loading_data = load_data(file_source)

sales_data = clean_data(loading_data)

def create_monthly_financial_chart(month_results):
    revenue_by_month = month_results["revenue_by_month"]
    cost_by_month = month_results["cost_by_month"]
    profit_by_month = month_results["profit_by_month"]

    monthly_figure,monthly_chart = plt.subplots(figsize=(10, 5))

    # Show case the revenue trend by month
    monthly_chart.plot(revenue_by_month.index.astype(str),revenue_by_month.values,c="black",label="Revenue line")

    # Show case the cost trend by month
    monthly_chart.plot(cost_by_month.index.astype(str),cost_by_month.values,c="red",label="Cost line")

    # Show case the profit trend by month
    monthly_chart.plot(profit_by_month.index.astype(str),profit_by_month.values,c="green",label="Profit line")

    # Label title and axsis
    monthly_chart.set_title("Monthly Financial Performance")
    monthly_chart.set_xlabel("Month and Year")
    monthly_chart.set_ylabel("Amount ($)")

    # Showcase the legend to make it clearer
    monthly_chart.legend()
    # More neat
    monthly_figure.tight_layout()

    return monthly_figure

product_result = analyze_products(sales_data)
def create_product_performance_chart(product_results):
    revenue_by_product = product_results["revenue_by_product"]
    profit_by_product = product_results["profit_by_product"]

    # Figuring out where they go in the x-axsis

    product_positions = list(range(len(revenue_by_product)))
    bar_width = 0.4

    revenue_positions = []
    profit_positions = []

    for position in product_positions:
        revenue_positions.append(position - bar_width / 2)
        profit_positions.append(position + bar_width / 2)

    product_figure, product_chart = plt.subplots(figsize=(10, 5))

    # Make the bars
    product_chart.bar(revenue_positions, revenue_by_product.values, width=bar_width, label="Revenue",color="blue")
    product_chart.bar(profit_positions, profit_by_product.values, width=bar_width, label="Profit",color="green")

    # Change the x-axsis names
    product_chart.set_xticks(product_positions)
    product_chart.set_xticklabels(revenue_by_product.index)

    # Add titles
    product_chart.set_title("Product Performance")
    product_chart.set_xlabel("Product")
    product_chart.set_ylabel("Amount ($)")

    # Showcase the legend to make it clearer
    product_chart.legend()

    # Make it neater
    product_figure.tight_layout()
    return product_figure

def create_region_performance_chart(region_results):

    revenue_by_region = region_results["revenue_by_region"]
    profit_by_region = region_results["profit_by_region"]

    bar_width = 0.4
    region_position = list(range(len(revenue_by_region)))
    revenue_postion = []
    profit_postion = []

    for postion in region_position:
        revenue_postion.append(postion - bar_width/2)
        profit_postion.append(postion + bar_width/2)

    # Make the canvas
    region_figure,region_chart = plt.subplots(figsize=(10, 5))

    # Make the bars
    region_chart.bar(revenue_postion,revenue_by_region.values,color="yellow",width=bar_width,label="Revenue of product")
    region_chart.bar(profit_postion,profit_by_region.values,color="green",width=bar_width,label="Profit of product")

    # Fixinig the increments
    region_chart.set_xticks(region_position)
    region_chart.set_xticklabels(revenue_by_region.index)

    # Add titles
    region_chart.set_title("Regional Performance")
    region_chart.set_ylabel("Amount ($)")
    region_chart.set_xlabel("Region")

    # Showcase the legend to make it clearer
    region_chart.legend()

    # Making it neater
    region_figure.tight_layout()
    return region_figure

def create_monthly_revenue_growth_chart(month_results):
    revenue_growth = month_results["revenue_growth"]

    revenue_figure,revenue_chart = plt.subplots(figsize=(10, 5))

    months = []

    for month in revenue_growth.keys():
        months.append(str(month))

    # Plot the graph
    revenue_chart.plot(months,revenue_growth.values(),c="green",label="Revenue Growth (%)")

    # Make the titels
    revenue_chart.set_title("Monthly Revenue Growth")
    revenue_chart.set_xlabel("Month")
    revenue_chart.set_ylabel("Revenue Growth (%)")

    # Show the legend
    revenue_chart.legend()

    # Tidy
    revenue_figure.tight_layout

    return revenue_figure


def create_product_sales_volume_chart(month_results):
    quantity_by_product_by_month = month_results["quantity_by_product_by_month"]

    products = []

    for index in quantity_by_product_by_month.index:
        product = index[1]

        if product not in products:
            products.append(product)

    product_volume_figure, product_volume_chart = plt.subplots(figsize=(10, 5))

    for product in products:
        months = []
        quantities = []

        for index in quantity_by_product_by_month.index:
            month = index[0]
            current_product = index[1]

            if current_product == product:
                months.append(str(month))
                quantities.append(quantity_by_product_by_month[index])

        product_volume_chart.plot(months, quantities, label=product)

    # set the titles   
    product_volume_chart.set_title("Product Sales Volume Over Time")
    product_volume_chart.set_xlabel("Month")
    product_volume_chart.set_ylabel("Quantity Sold")
    # Show the legend
    product_volume_chart.legend()

    # Make it neat
    product_volume_figure.tight_layout()

    return product_volume_figure










    