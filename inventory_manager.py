import pandas as pd
import numpy as np
import os
from datetime import datetime

INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales_log.csv"
LOW_STOCK_THRESHOLD = 10


# ---------- DATA LOADING & SAVING ----------

def load_inventory():
    """Load inventory from CSV, or create an empty one if it doesn't exist."""
    if os.path.exists(INVENTORY_FILE):
        return pd.read_csv(INVENTORY_FILE)
    else:
        return pd.DataFrame(columns=["ProductID", "Name", "Category", "Price", "Quantity"])


def save_inventory(df):
    df.to_csv(INVENTORY_FILE, index=False)


def load_sales():
    if os.path.exists(SALES_FILE):
        return pd.read_csv(SALES_FILE)
    else:
        return pd.DataFrame(columns=["ProductID", "Name", "QuantitySold", "Revenue", "Date"])


def save_sales(df):
    df.to_csv(SALES_FILE, index=False)


# ---------- CORE FEATURES ----------

def add_product(df, product_id, name, category, price, quantity):
    """Add a new product, or update quantity if it already exists."""
    if product_id in df["ProductID"].values:
        df.loc[df["ProductID"] == product_id, "Quantity"] += quantity
        print(f"Updated stock for '{name}'. New quantity: "
              f"{df.loc[df['ProductID'] == product_id, 'Quantity'].values[0]}")
    else:
        new_row = pd.DataFrame([{
            "ProductID": product_id, "Name": name, "Category": category,
            "Price": price, "Quantity": quantity
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        print(f"Added new product '{name}' with quantity {quantity}.")
    return df


def record_sale(inventory_df, sales_df, product_id, quantity_sold):
    """Reduce stock and log the sale. Returns updated (inventory_df, sales_df)."""
    if product_id not in inventory_df["ProductID"].values:
        print("Product not found.")
        return inventory_df, sales_df

    row = inventory_df.loc[inventory_df["ProductID"] == product_id]
    available = row["Quantity"].values[0]

    if quantity_sold > available:
        print(f"Not enough stock. Only {available} units available.")
        return inventory_df, sales_df

    price = row["Price"].values[0]
    name = row["Name"].values[0]
    revenue = price * quantity_sold

    inventory_df.loc[inventory_df["ProductID"] == product_id, "Quantity"] -= quantity_sold

    new_sale = pd.DataFrame([{
        "ProductID": product_id, "Name": name, "QuantitySold": quantity_sold,
        "Revenue": revenue, "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    sales_df = pd.concat([sales_df, new_sale], ignore_index=True)

    print(f"Sold {quantity_sold} units of '{name}' for ₹{revenue:.2f}.")
    return inventory_df, sales_df


def search_product(df, keyword):
    result = df[df["Name"].str.contains(keyword, case=False, na=False)]
    if result.empty:
        print("No matching products found.")
    else:
        print(result.to_string(index=False))
    return result


def check_low_stock(df):
    """Uses NumPy to flag products below the threshold."""
    quantities = df["Quantity"].to_numpy()
    low_mask = quantities < LOW_STOCK_THRESHOLD
    low_stock_items = df[low_mask]

    if low_stock_items.empty:
        print("All products are sufficiently stocked.")
    else:
        print(f"\n⚠ LOW STOCK ALERT (below {LOW_STOCK_THRESHOLD} units):")
        print(low_stock_items[["Name", "Quantity"]].to_string(index=False))
    return low_stock_items


def generate_report(inventory_df, sales_df):
    """Generate a summary business report."""
    print("\n" + "=" * 45)
    print("           INVENTORY REPORT")
    print("=" * 45)

    if inventory_df.empty:
        print("Inventory is empty.")
        return

    total_value = np.sum(inventory_df["Price"].to_numpy() * inventory_df["Quantity"].to_numpy())
    print(f"Total Products       : {len(inventory_df)}")
    print(f"Total Stock Units    : {int(inventory_df['Quantity'].sum())}")
    print(f"Total Inventory Value: ₹{total_value:,.2f}")

    if not sales_df.empty:
        total_revenue = sales_df["Revenue"].sum()
        top_seller = sales_df.groupby("Name")["QuantitySold"].sum().idxmax()
        top_units = sales_df.groupby("Name")["QuantitySold"].sum().max()
        print(f"Total Revenue        : ₹{total_revenue:,.2f}")
        print(f"Top-Selling Product  : {top_seller} ({top_units} units sold)")
    else:
        print("No sales recorded yet.")

    print("=" * 45)


# ---------- MENU-DRIVEN CLI ----------

def main():
    inventory_df = load_inventory()
    sales_df = load_sales()

    menu = """
--- INVENTORY MANAGEMENT SYSTEM ---
1. Add / Restock Product
2. Record a Sale
3. Search Product
4. View Low Stock Alerts
5. Generate Report
6. View Full Inventory
7. Save & Exit
Choose an option (1-7): """

    while True:
        choice = input(menu).strip()

        if choice == "1":
            pid = input("Product ID: ").strip()
            name = input("Name: ").strip()
            category = input("Category: ").strip()
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            inventory_df = add_product(inventory_df, pid, name, category, price, qty)

        elif choice == "2":
            pid = input("Product ID to sell: ").strip()
            qty = int(input("Quantity sold: "))
            inventory_df, sales_df = record_sale(inventory_df, sales_df, pid, qty)

        elif choice == "3":
            keyword = input("Search by name: ").strip()
            search_product(inventory_df, keyword)

        elif choice == "4":
            check_low_stock(inventory_df)

        elif choice == "5":
            generate_report(inventory_df, sales_df)

        elif choice == "6":
            print(inventory_df.to_string(index=False) if not inventory_df.empty else "Inventory is empty.")

        elif choice == "7":
            save_inventory(inventory_df)
            save_sales(sales_df)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
