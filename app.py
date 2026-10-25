import streamlit as st
import pandas as pd
from data_processing import load_data, validate_data, clean_data
from analysis import calculate_overall_metrics, analyze_products, analyze_regions, analyze_months
from charts import create_monthly_financial_chart, create_product_performance_chart, create_region_performance_chart, create_monthly_revenue_growth_chart, create_product_sales_volume_chart

# Title for my user interface
st.title("Sales Analytics Dashboard")

# Upload data
uploaded_file = st.file_uploader("Upload your sales file(Excel/CSV):", type=["xlsx", "csv"])

# Use panda to load the data
if uploaded_file is not None:
    sales_data = load_data(uploaded_file)


    # Check if data is valid
    errors =  validate_data(sales_data)

    if len(errors) > 0:
        for erorr in errors:
            st.error(erorr)
        st.stop()

    # Data is valid so cleaning it now 
    sales_data = clean_data(sales_data)

    # Filter work
    products = sales_data["Product"].unique()
    selected_products = st.sidebar.multiselect("Product", products, default=products)
    product_filter = sales_data["Product"].isin(selected_products)

    regions = sales_data["Region"].unique()
    selected_regions = st.sidebar.multiselect("Region", regions, default=regions)
    region_filter = sales_data["Region"].isin(selected_regions)

    filtered_sales_data = sales_data[product_filter & region_filter]

    if filtered_sales_data.empty:
        st.error("No sales records match the selected filters.")
        st.stop()

    # Analysis
    overall_results = calculate_overall_metrics(filtered_sales_data)
    product_results = analyze_products(filtered_sales_data)
    region_results = analyze_regions(filtered_sales_data)
    month_results = analyze_months(filtered_sales_data)


    # Cards
    kpi_columns = st.columns(3)

    kpi_columns[0].metric("Total Revenue", f"${overall_results['total_revenue']:,.0f}")
    kpi_columns[1].metric("Total Cost", f"${overall_results['total_cost']:,.0f}")
    kpi_columns[2].metric("Total Profit", f"${overall_results['total_profit']:,.0f}")

    kpi_columns_2 = st.columns(3)

    kpi_columns_2[0].metric("Profit Margin", f"{overall_results['overall_profit_margin']:.0f}%")
    kpi_columns_2[2].metric("Quantity Sold", f"{overall_results['total_quantity']:,.0f}")


    # Making charts
    # Monthly Financial Performance
    st.subheader("Monthly Financial Performance")
    monthly_figure = create_monthly_financial_chart(month_results)
    st.pyplot(monthly_figure)

    # Product and Region charts side by side
    chart_columns = st.columns(2)

    product_figure = create_product_performance_chart(product_results)
    region_figure = create_region_performance_chart(region_results)

    chart_columns[0].subheader("Product Performance")
    chart_columns[0].pyplot(product_figure)

    chart_columns[1].subheader("Regional Performance")
    chart_columns[1].pyplot(region_figure)

    # Monthly Revenue Growth
    st.subheader("Monthly Revenue Growth")
    growth_figure = create_monthly_revenue_growth_chart(month_results)
    st.pyplot(growth_figure)

    # Product Sales Volume Over Time
    st.subheader("Product Sales Volume Over Time")
    volume_figure = create_product_sales_volume_chart(month_results)
    st.pyplot(volume_figure)

    # Table 
    product_table = pd.DataFrame({
        "Revenue": product_results["revenue_by_product"],
        "Cost": product_results["cost_by_product"],
        "Profit": product_results["profit_by_product"],
        "Profit Margin": product_results["profit_margin_by_product"],
        "Quantity Sold": product_results["quantity_by_product"]})

    st.subheader("Product Details")
    st.dataframe(product_table)