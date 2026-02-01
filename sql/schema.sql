-- Undropable tables (FOR THIS DATASET)
CREATE TABLE IF NOT EXISTS dim_date (
    Date_key INTEGER PRIMARY KEY, --YYYYMMDD
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name TEXT,
    week INTEGER,
    day_of_month INTEGER,
    day_of_week INTEGER,
    day_name TEXT,
    is_weekend INTEGER,
    UNIQUE(full_date)
);

CREATE TABLE IF NOT EXISTS dim_time (
    Time_key INTEGER PRIMARY KEY, -- minutes from midnight (0–1439)
    hour INTEGER,
    minute INTEGER
);


-- DROPABLE TABLES
CREATE TABLE IF NOT EXISTS dim_customers(
    Customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_id INTEGER NOT NULL,
    Customer_Segment TEXT,
    Customer_Country TEXT,
    Customer_State TEXT,
    Customer_City TEXT,
    UNIQUE(Customer_id)
);

CREATE TABLE IF NOT EXISTS dim_product(
    Product_key INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_Card_Id INTEGER NOT NULL,
    Product_Category_Id INTEGER,
    Category_Name TEXT,
    Product_Name TEXT,
    Product_Price REAL,
    Department_Id INTEGER,
    Department_Name TEXT,
    Product_Status INTEGER,
    UNIQUE(Product_Card_Id)
);

CREATE TABLE IF NOT EXISTS dim_shipping (
    Shipping_key INTEGER PRIMARY KEY AUTOINCREMENT,
    Shipping_Mode TEXT,
    Delivery_Status TEXT,
    Is_Late INTEGER,
    Days_for_shipment_scheduled INTEGER
);

CREATE TABLE IF NOT EXISTS fact_orders (
    order_key INTEGER PRIMARY KEY AUTOINCREMENT,
    
    Date_key INTEGER, 
    Shipping_Date_key INTEGER,
    Time_key INTEGER, 
    Customer_key INTEGER,
    Product_key INTEGER,
    Shipping_key INTEGER,
    
    Order_Id INTEGER NOT NULL,
    Order_Item_Id INTEGER NOT NULL,
    Order_Customer_Id INTEGER,
    Order_Item_Cardprod_Id INTEGER,
    
    Order_Item_Quantity INTEGER,
    Sales REAL, 
    Order_Item_Total REAL,
    Order_Profit_Per_Order REAL,
    Order_Item_Profit_Ratio REAL,
    Order_Item_Discount REAL,
    Order_Item_Discount_Rate REAL,
    Order_Item_Product_Price REAL,
    
    Days_For_Shipping_Real INTEGER,
    Profit_Margin_Pct REAL,
    High_Loss_Flag INTEGER,
    
    Market TEXT,
    Order_Region TEXT,
    Order_Country TEXT,
    Order_City TEXT,
    Order_State TEXT,
    Order_Status TEXT,
    
    FOREIGN KEY (Date_key) REFERENCES dim_date(Date_key),
    FOREIGN KEY (Shipping_Date_key) REFERENCES dim_date(Date_key),
    FOREIGN KEY (Time_key) REFERENCES dim_time(Time_key),
    FOREIGN KEY (Customer_key) REFERENCES dim_customers(Customer_key),
    FOREIGN KEY (Product_key) REFERENCES dim_product(Product_key),
    FOREIGN KEY (Shipping_key) REFERENCES dim_shipping(Shipping_key)
);


-- Fill dim_date
WITH RECURSIVE dates(d) AS (
    SELECT date('2015-01-01')
    UNION ALL
    SELECT date(d, '+1 day')
    FROM dates
    WHERE d < date('2018-12-31')
)
INSERT INTO dim_date (
    Date_key,
    full_date,
    year,
    quarter,
    month,
    month_name,
    week,
    day_of_month,
    day_of_week,
    day_name,
    is_weekend
)
SELECT
    CAST(strftime('%Y%m%d', d) AS INTEGER) AS Date_key,
    d AS full_date,
    CAST(strftime('%Y', d) AS INTEGER) AS year,
    ((CAST(strftime('%m', d) AS INTEGER) - 1) / 3) + 1 AS quarter,
    CAST(strftime('%m', d) AS INTEGER) AS month,
    CASE strftime('%m', d)
        WHEN '01' THEN 'January'
        WHEN '02' THEN 'February'
        WHEN '03' THEN 'March'
        WHEN '04' THEN 'April'
        WHEN '05' THEN 'May'
        WHEN '06' THEN 'June'
        WHEN '07' THEN 'July'
        WHEN '08' THEN 'August'
        WHEN '09' THEN 'September'
        WHEN '10' THEN 'October'
        WHEN '11' THEN 'November'
        WHEN '12' THEN 'December'
    END AS month_name,
    CAST(strftime('%W', d) AS INTEGER) AS week,
    CAST(strftime('%d', d) AS INTEGER) AS day_of_month,
    CAST(strftime('%w', d) AS INTEGER) AS day_of_week,
    CASE strftime('%w', d)
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
    END AS day_name,
    CASE
        WHEN strftime('%w', d) IN ('0','6') THEN 1
        ELSE 0
    END AS is_weekend
FROM dates;

-- Fill dim_time
WITH RECURSIVE minutes(m) AS (
    SELECT 0
    UNION ALL
    SELECT m + 1
    FROM minutes
    WHERE m < 1439
)
INSERT INTO dim_time (Time_key, hour, minute)
SELECT
    m AS Time_key,
    m / 60 AS hour,
    m % 60 AS minute
FROM minutes;