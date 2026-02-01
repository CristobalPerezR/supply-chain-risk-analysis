import pandas as pd
from pandera.errors import SchemaErrors
from ..utils.dataframe_schemas import csv_schema
from ..utils.errors import ValidationError

def transform(df:pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=['Product Image','Product Description','Customer Email','Customer Password', 'Category Id',
                     'Customer Fname','Customer Lname', 'Customer Street', 'Type', 'Customer Zipcode', 'Order Zipcode', 'Latitude', 'Longitude'], inplace=True)
    
    df['Datetime Order'] = pd.to_datetime(df['order date (DateOrders)'], format="%m/%d/%Y %H:%M") # str -> Datetime
    df['Datetime Shipping'] = pd.to_datetime(df['shipping date (DateOrders)'], format="%m/%d/%Y %H:%M") # str -> Datetime
    

    ########## NEW COLUMS ##############
    df['Order Hour'] = df['Datetime Order'].dt.hour # int (0-23)
    df['Order Minute'] = df['Datetime Order'].dt.minute # int (0-59)
    df['Order Date'] = df['Datetime Order'].dt.date # Date yyyy-mm-dd

    df['Shipping Hour'] = df['Datetime Shipping'].dt.hour # int (0-23)
    df['Shipping Minute'] = df['Datetime Shipping'].dt.minute # int (0-59)
    df['Shipping Date'] = df['Datetime Shipping'].dt.date # Date yyyy-mm-dd

    df['Order Time Period'] = pd.cut(
        df['Order Hour'].fillna(-1),
        bins=[-1, 0, 6, 12, 18, 24],
        labels=['Invalid', 'Dawn', 'Morning', 'Afternoon', 'Night'],
        include_lowest=True
    ).astype('category')

    df['Profit Margin Pct'] = (df['Order Profit Per Order'] / df['Sales'].replace(0, pd.NA)) * 100
    df['High Loss Flag'] = (df['Order Profit Per Order'] < -1000000000).astype('Int8') # Arbitrary Treshold, can be redefined

    ######### STANDARIZE NAMES ############
    df.drop(columns=['order date (DateOrders)', 'shipping date (DateOrders)'], inplace=True)

    df.rename(columns={'Category Name' : 'Product Category Name', 'Late_delivery_risk' : 'Is Late'}, inplace=True)

    df.columns = (
        df.columns
          .str.replace(' ', '_', regex=False)
          .str.replace('(', '', regex=False)
          .str.replace(')', '', regex=False)
          .str.lower()
    )

    try:
        validated_df = csv_schema.validate(df, lazy=True)
        print("Schema validated")
    except SchemaErrors as e:
        raise ValidationError(f'Schema failed: \n{e}')

    return validated_df