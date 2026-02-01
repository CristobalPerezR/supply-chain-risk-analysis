from src.dataset.download import download_dataset
from src.db_scripts.init_db import init_db
from src.etl.extract import extract_from_csv
from src.etl.transform import transform
from src.etl.load import load_to_sqlite, save_as_csv

print("\n================= DOWNLOAD PROCESS =================\n")

file_path = download_dataset()

print("\n================= DB INITIALIZATION =================\n")

init_db("supply_chain_risk")

print("\n================= EXTRACTION PROCESS =================\n")

df = extract_from_csv(file_path)

print("\n================= TRANSFORMATION PROCESS =================\n")

df_transformed = transform(df)

print("\n================= LOAD PROCESS =================\n")

load_to_sqlite(df_transformed)
# save_as_csv(df_transformed)

# print("\n================= ETL FINISHED =================\n")