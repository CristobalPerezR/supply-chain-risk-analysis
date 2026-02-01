PRAGMA foreign_keys = OFF;

DELETE FROM fact_orders;
DELETE FROM sqlite_sequence WHERE name='fact_orders';

DELETE FROM dim_shipping;
DELETE FROM sqlite_sequence WHERE name='dim_shipping';

DELETE FROM dim_customers;
DELETE FROM sqlite_sequence WHERE name='dim_customers';

DELETE FROM dim_product;
DELETE FROM sqlite_sequence WHERE name='dim_product';

PRAGMA foreign_keys = ON;