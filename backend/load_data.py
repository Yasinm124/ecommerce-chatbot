import pandas as pd
from sqlalchemy import create_engine, text

# MySQL connection details
username = "root"          # your MySQL username
password = "root"  # replace with your MySQL password
host = "localhost"
port = "3306"
database = "ecommerce"

# Create MySQL engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

try:
    with engine.begin() as conn:
        # Disable foreign key checks
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))

        print("Loading users...")
        users = pd.read_csv("archive/users.csv")
        users.to_sql('users', conn, if_exists='replace', index=False)

        print("Loading products...")
        products = pd.read_csv("archive/products.csv")
        products.to_sql('products', conn, if_exists='replace', index=False)

        print("Loading orders...")
        orders = pd.read_csv("archive/orders.csv")
        orders.to_sql('orders', conn, if_exists='replace', index=False)

        print("Loading order items...")
        order_items = pd.read_csv("archive/order_items.csv")
        order_items.to_sql('order_items', conn, if_exists='replace', index=False)

        print("Loading distribution centers...")
        distribution_centers = pd.read_csv("archive/distribution_centers.csv")
        distribution_centers.to_sql('distribution_centers', conn, if_exists='replace', index=False)

        # Enable foreign key checks
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

    print("✅ All data inserted successfully into MySQL database!")

except Exception as e:
    print("❌ Error:", e)