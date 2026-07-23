from pathlib import Path
import urllib.parse
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load .env from project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

print(f"Server: {server}")
print(f"Database: {database}")
print(f"User: {username}")
print(f"Password loaded: {password is not None}")

# SQL Server connection string
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}",
    fast_executemany=True,
)

raw_folder = Path(__file__).resolve().parents[2] / "data/raw"

tables = {
    "categories.csv": "Categories",
    "customers.csv": "Customers",
    "stores.csv": "Stores",
    "suppliers.csv": "Suppliers",
    "promotions.csv": "Promotions",
    "products.csv": "Products",
    "orders.csv": "Orders",
    "order_items.csv": "OrderItems",
    "payments.csv": "Payments",
    "shipments.csv": "Shipments",
    "returns.csv": "Returns",
    "employees.csv": "Employees",
}

rename_map = {
    "category_id": "CategoryID",
    "category_name": "CategoryName",
    "customer_id": "CustomerID",
    "city": "City",
    "signup_date": "SignupDate",
    "store_id": "StoreID",
    "supplier_id": "SupplierID",
    "country": "Country",
    "promotion_id": "PromotionID",
    "discount": "Discount",
    "product_id": "ProductID",
    "price": "Price",
    "order_id": "OrderID",
    "order_date": "OrderDate",
    "order_item_id": "OrderItemID",
    "qty": "Qty",
    "payment_id": "PaymentID",
    "amount": "Amount",
    "shipment_id": "ShipmentID",
    "status": "Status",
    "return_id": "ReturnID",
    "refund": "Refund",
    "employee_id": "EmployeeID",
    "salary": "Salary",
}

for csv_file, table in tables.items():
    print(f"\nLoading {csv_file}...")

    df = pd.read_csv(raw_folder / csv_file)

    # Rename columns to match SQL table
    df.rename(columns=rename_map, inplace=True)

    print(df.columns.tolist())

    # Convert date columns
    if "SignupDate" in df.columns:
        df["SignupDate"] = pd.to_datetime(df["SignupDate"])

    if "OrderDate" in df.columns:
        df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    print("About to insert...")

    from sqlalchemy import text

    with engine.connect() as conn:
        print("Database:", conn.execute(text("SELECT DB_NAME()")).scalar())
        print("Server:", conn.execute(text("SELECT @@SERVERNAME")).scalar())
        print("Category Count:", conn.execute(text("SELECT COUNT(*) FROM Categories")).scalar())

    with engine.begin() as conn:
        df.to_sql(
            table,
            conn,
            if_exists="append",
            index=False,
            chunksize=1000,
        )

    print("Insert complete!")
    print(f"Loaded {len(df):,} rows into {table}")

print("\nAll tables loaded successfully!")