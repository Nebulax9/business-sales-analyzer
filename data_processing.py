import pandas as pd


def load_data(file_source):
    sales_data = pd.read_excel(file_source)
    return sales_data


def validate_data(sales_data):
    errors = []

    # Check if the file even has data to begin with
    if sales_data.empty:
        errors.append("The file has no Data. Please try again with the appropriate data/file: )")

    # Check if all required columns are correct
    missing_columns = []
    required_columns = ["Date", "Product", "Region", "Revenue", "Cost", "Quantity"]

    for column in required_columns:
        if column not in sales_data.columns:
            missing_columns.append(column)

    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")

    # Check if required columns contain missing values
    for column in required_columns:
        if column in sales_data.columns:
            missing_count = sales_data[column].isna().sum()

            if missing_count > 0:
                errors.append(f"{column} contains {missing_count} missing values.")

    # Check numeric columns
    numeric_columns = ["Revenue", "Cost", "Quantity"]

    for column in numeric_columns:
        if column in sales_data.columns:
            try:
                pd.to_numeric(sales_data[column])
            except:
                errors.append(f"{column} contains invalid numeric values.")

    # Check if Date can be treated as a real date
    if "Date" in sales_data.columns:
        try:
            pd.to_datetime(sales_data["Date"])
        except:
            errors.append("The Date column contains a value that cannot be treated as a date.")

    return errors