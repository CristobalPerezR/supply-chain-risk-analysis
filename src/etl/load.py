import pandas as pd
from ..utils.db import insert_dataframe, get_connection, execute_script, fetch_query
import os

clear_tables = os.path.join("sql", "clear_tables.sql") # SCRIPT

filter_customers = ['customer_id',
                    'customer_segment',
                    'customer_country',
                    'customer_state',
                    'customer_city']

filter_product = ['product_card_id',
                'product_category_id',
                'product_category_name',
                'product_name',
                'product_price',
                'department_id',
                'department_name',
                'product_status']

filter_shipping = ['shipping_mode',
                      'delivery_status',
                      'is_late',
                      'days_for_shipment_scheduled']

filter_orders = ['order_id',
                 'order_item_id',
                 'order_customer_id',
                 'order_item_cardprod_id',
                 'order_item_quantity',
                 'sales',
                 'order_item_total',
                 'order_profit_per_order',
                 'order_item_profit_ratio',
                 'order_item_discount',
                 'order_item_discount_rate',
                 'order_item_product_price',
                 'days_for_shipping_real',
                 'profit_margin_pct',
                 'high_loss_flag',
                 'market',
                 'order_region',
                 'order_country',
                 'order_city',
                 'order_state',
                 'order_status']

def load_to_sqlite(df:pd.DataFrame) -> int:
    dim_customers = df[filter_customers].drop_duplicates(subset=['Customer_id'])
    dim_product = df[filter_product]
    dim_shipping = df[filter_shipping]
    fact_orders = df[filter_orders]

    with get_connection() as conn:
        execute_script(conn, clear_tables)
        insert_dataframe(conn, dim_customers, 'dim_customers')
        res = fetch_query(conn, """SELECT * FROM dim_customers;""")
        print(res)
    return 0


def save_as_csv(df:pd.DataFrame) -> int:
    return 0