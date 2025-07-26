import pandas as pd

# Load CSV files
orders = pd.read_csv("archive/orders.csv")
order_items = pd.read_csv("archive/order_items.csv")
products = pd.read_csv("archive/products.csv")
users = pd.read_csv("archive/users.csv")
distribution = pd.read_csv("archive/distribution_centers.csv")

# Merge order_items with orders (based on order_id)
order_data = pd.merge(order_items, orders, on="order_id", how="left")

# Merge with products (based on product_id)
order_data = pd.merge(order_data, products, on="id", how="left")

# Merge with users (based on user_id)
order_data = pd.merge(order_data, users, on="id", how="left")

# Merge with distribution centers (based on distribution_center_id)
order_data = pd.merge(order_data, distribution, on="id", how="left")

# Save in smaller chunks to avoid storage issues
for i, start in enumerate(range(0, len(order_data), 50000)):
    chunk = order_data.iloc[start:start+50000]
    chunk.to_csv(f"ecommerce_data_part_{i}.csv", index=False)

print("✅ Data saved in smaller files: ecommerce_data_part_0.csv, ecommerce_data_part_1.csv, ...")
