import pandas as pd
from pandera.pandas import DataFrameSchema, Column
from ..utils.db_etl import get_connection, insert_dataframe
from ..utils.errors import InsertionError, ValidationError

raw_schema = DataFrameSchema({
    "Type": Column(str, nullable=True, coerce=True),
    "Days for shipping (real)": Column("Int64", nullable=True, coerce=True),
    'Days for shipment (scheduled)': Column("Int64", nullable=True, coerce=True),
    'Benefit per order': Column(float, nullable=True, coerce=True),
    'Sales per customer': Column(float, nullable=True, coerce=True),
    'Delivery Status': Column(str, nullable=True, coerce=True),
    'Late_delivery_risk': Column("Int64", nullable=True, coerce=True),
    'Category Id': Column("Int64", nullable=True, coerce=True),
    'Category Name': Column(str, nullable=True, coerce=True),
    'Customer City': Column(str, nullable=True, coerce=True),
    'Customer Country': Column(str, nullable=True, coerce=True),
    'Customer Email': Column(str, nullable=True, coerce=True),
    'Customer Fname': Column(str, nullable=True, coerce=True),
    'Customer Id': Column("Int64", nullable=True, coerce=True),
    'Customer Lname': Column(str, nullable=True, coerce=True),
    'Customer Password': Column(str, nullable=True, coerce=True),
    'Customer Segment': Column(str, nullable=True, coerce=True),
    'Customer State': Column(str, nullable=True, coerce=True),
    'Customer Street': Column(str, nullable=True, coerce=True),
    'Customer Zipcode': Column(str, nullable=True, coerce=True),
    'Department Id': Column("Int64", nullable=True, coerce=True),
    'Department Name': Column(str, nullable=True, coerce=True),
    'Latitude': Column(float, nullable=True, coerce=True),
    'Longitude': Column(float, nullable=True, coerce=True),
    'Market': Column(str, nullable=True, coerce=True),
    'Order City': Column(str, nullable=True, coerce=True),
    'Order Country': Column(str, nullable=True, coerce=True),
    'Order Customer Id': Column("Int64", nullable=True, coerce=True),
    'order date (DateOrders)': Column(str, nullable=True, coerce=True),
    'Order Id': Column("Int64", nullable=True, coerce=True),
    'Order Item Cardprod Id': Column("Int64", nullable=True, coerce=True),
    'Order Item Discount': Column(float, nullable=True, coerce=True),
    'Order Item Discount Rate': Column(float, nullable=True, coerce=True),
    'Order Item Id': Column("Int64", nullable=True, coerce=True),
    'Order Item Product Price': Column(float, nullable=True, coerce=True),
    'Order Item Profit Ratio': Column(float, nullable=True, coerce=True),
    'Order Item Quantity': Column("Int64", nullable=True, coerce=True),
    'Sales': Column(float, nullable=True, coerce=True),
    'Order Item Total': Column(float, nullable=True, coerce=True),
    'Order Profit Per Order': Column(float, nullable=True, coerce=True),
    'Order Region': Column(str, nullable=True, coerce=True),
    'Order State': Column(str, nullable=True, coerce=True),
    'Order Status': Column(str, nullable=True, coerce=True),
    'Order Zipcode': Column(str, nullable=True, coerce=True),
    'Product Card Id': Column("Int64", nullable=True, coerce=True),
    'Product Category Id': Column("Int64", nullable=True, coerce=True),
    'Product Description': Column(str, nullable=True, coerce=True),
    'Product Image': Column(str, nullable=True, coerce=True),
    'Product Name': Column(str, nullable=True, coerce=True),
    'Product Price': Column(float, nullable=True, coerce=True),
    'Product Status': Column("Int64", nullable=True, coerce=True),
    'shipping date (DateOrders)': Column(str, nullable=True, coerce=True),
    'Shipping Mode': Column(str, nullable=True, coerce=True),
})

def extract_validate_save(data_path: str) -> int:
    df = pd.read_csv(data_path, sep=",", na_values="?", encoding='latin1')
    try:
        valid = raw_schema.validate(df)
        print("Extract_Process: Schema validated")
        try:
            with get_connection() as conn:
                insert_dataframe(conn, valid, "supply_chain_risk_raw_typed")
            print("Extract_Process: Dataframe inserted into table: [supply_chain_risk_raw_typed]")
        except Exception as e:
            raise InsertionError(f"Extract_Process: Insertion failed: {e}")
        return 1
    except Exception as e:
        raise ValidationError(f"Extract_Process: Schema not valid: {e}")