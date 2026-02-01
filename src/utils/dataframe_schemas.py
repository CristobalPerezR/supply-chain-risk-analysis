import pandera as pa
from pandera.pandas import DataFrameSchema, Column, Check

csv_schema = DataFrameSchema({
    ### INT64
    "days_for_shipping_real" : Column(pa.Int64, coerce=True, checks=Check.ge(0)),
    "days_for_shipment_scheduled" : Column(pa.Int64, coerce=True, checks=Check.ge(0)),
    "customer_id" : Column(pa.Int64, coerce=True, required=True, nullable=False),
    "department_id" : Column(pa.Int64, coerce=True),
    "order_customer_id" : Column(pa.Int64, coerce=True),
    "order_id" : Column(pa.Int64, coerce=True, required=True, nullable=False),
    "order_item_cardprod_id" : Column(pa.Int64, coerce=True),
    "order_item_id" : Column(pa.Int64, coerce=True),
    "order_item_quantity" : Column(pa.Int64, coerce=True, checks=Check.ge(1)),
    "product_card_id" : Column(pa.Int64, coerce=True),
    "product_category_id" : Column(pa.Int64, coerce=True),

    # FLOATS
    "benefit_per_order" : Column(pa.Float64, coerce=True),
    "sales_per_customer" : Column(pa.Float64, coerce=True),
    "order_item_discount" : Column(pa.Float64, coerce=True, checks=Check.ge(0)),
    "order_item_discount_rate": Column(pa.Float64, coerce=True, checks=[Check.ge(0), Check.le(1)]),
    "order_item_product_price": Column(pa.Float64, coerce=True, checks=Check.ge(0)),
    "order_item_profit_ratio" : Column(pa.Float64, coerce=True),
    "order_item_total": Column(pa.Float64, coerce=True, checks=Check.ge(0)),
    "order_profit_per_order" : Column(pa.Float64, coerce=True),
    "product_price": Column(pa.Float64, coerce=True, checks=Check.ge(0)),
    "profit_margin_pct" : Column(pa.Float64, coerce=True),
    "sales": Column(pa.Float64, coerce=True, checks=Check.ge(0)),

    # STRINGS
    "delivery_status" : Column(str, coerce=True),
    "product_category_name" : Column(str, coerce=True),
    "customer_city" : Column(str, coerce=True),
    "customer_country" : Column(str, coerce=True),
    "customer_segment" : Column(str, coerce=True),
    "customer_state" : Column(str, coerce=True),
    "department_name" : Column(str, coerce=True),
    "market" : Column(str, coerce=True),
    "order_city" : Column(str, coerce=True),
    "order_country" : Column(str, coerce=True),
    "order_region" : Column(str, coerce=True),
    "order_state" : Column(str, coerce=True),
    "order_status" : Column(str, coerce=True),
    "product_name" : Column(str, coerce=True),
    "shipping_mode" : Column(str, coerce=True),

    #DATES
    "datetime_order" : Column(pa.Timestamp, coerce=True),
    "shipping_date" : Column(pa.Timestamp, coerce=True),
    "order_date" : Column(pa.Timestamp, coerce=True),
    "datetime_shipping" : Column(pa.Timestamp, coerce=True),

    # MINUTES AND HOURS
    "order_hour": Column(pa.Int32, coerce=True, checks=Check.between(0, 23)),
    "order_minute": Column(pa.Int32, coerce=True, checks=Check.between(0, 59)),
    "shipping_hour": Column(pa.Int32, coerce=True, checks=Check.between(0, 23)),
    "shipping_minute": Column(pa.Int32, coerce=True, checks=Check.between(0, 59)),

    # CATEGORY
    "order_time_period" : Column(pa.Category, coerce=True),
    
    # BOOL
    "is_late" : Column(pa.Int8, coerce=True, checks=Check.isin([0,1])),
    "product_status" : Column(pa.Int8, coerce=True, checks=Check.isin([0,1])),
    "high_loss_flag" : Column(pa.Int8, coerce=True, checks=Check.isin([0,1])),
},
    strict=True,
    ordered=False,
)