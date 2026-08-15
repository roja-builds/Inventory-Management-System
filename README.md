# 📦 Inventory Management System

A smart and simple **Inventory Management System** developed using **Python, Pandas, and NumPy**. It is a command-line application designed to manage product stock, record sales, search products, identify low-stock items, and generate useful business reports.

## ✨ Features

* ➕ Add / Restock Products
* 💰 Record Sales
* 🔍 Search Products
* ⚠️ Low Stock Alerts
* 📊 Generate Inventory Reports
* 📦 View Full Inventory
* 💾 Save Inventory and Sales Data
* 🧾 CSV-based Data Storage

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **CSV File Handling**

## 📌 Project Overview

This project provides a menu-driven command-line interface for managing inventory efficiently.

The system maintains two types of data:

* **Inventory Data** – Product ID, Name, Category, Price, and Quantity
* **Sales Data** – Product ID, Product Name, Quantity Sold, Revenue, and Date

The inventory and sales information are stored using CSV files.

## 🚀 Key Functionalities

### 1. Add / Restock Product

Users can add a new product with its:

* Product ID
* Product Name
* Category
* Price
* Quantity

If the product already exists, its quantity is updated instead of creating a duplicate product.

### 2. Record a Sale

Users can record product sales by entering the Product ID and quantity sold.

The system:

* Checks whether the product exists
* Checks available stock
* Reduces the stock quantity
* Calculates revenue
* Records the sale with date and time

### 3. Search Product

Users can search for products by name using a keyword. The search is case-insensitive.

### 4. Low Stock Alert

The system checks product quantities and identifies products with stock below the defined threshold.

**Low Stock Threshold: 10 units**

### 5. Generate Business Report

The report provides:

* Total number of products
* Total stock units
* Total inventory value
* Total revenue
* Top-selling product
* Number of units sold

NumPy is used for inventory value calculation, while Pandas is used for sales analysis.

## 🖥️ Menu

```text
--- INVENTORY MANAGEMENT SYSTEM ---

1. Add / Restock Product
2. Record a Sale
3. Search Product
4. View Low Stock Alerts
5. Generate Report
6. View Full Inventory
7. Save & Exit

Choose an option (1-7):
```

## 🧪 Sample Input & Output

### ➕ Add Product

**Input:**

```text
Choose an option (1-7): 1

Product ID: P101
Name: Laptop
Category: Electronics
Price: 50000
Quantity: 15
```

**Output:**

```text
Added new product 'Laptop' with quantity 15.
```

### 💰 Record a Sale

**Input:**

```text
Choose an option (1-7): 2

Product ID to sell: P101
Quantity sold: 3
```

**Output:**

```text
Sold 3 units of 'Laptop' for ₹150000.00.
```

### ⚠️ Low Stock Alert

**Output:**

```text
⚠ LOW STOCK ALERT (below 10 units):

Name      Quantity
Keyboard  5
Mouse     7
```

The program displays this alert when products fall below the configured threshold.

### 📊 Inventory Report

**Output:**

```text
=============================================
 INVENTORY REPORT
=============================================
Total Products : 1
Total Stock Units : 12
Total Inventory Value: ₹600000.00
Total Revenue : ₹150000.00
Top-Selling Product : Laptop (3 units sold)
=============================================
```

## 📂 Project Structure

```text
inventory-management-system/
│
├── inventory_manager.py
├── inventory.csv
├── sales_log.csv
└── README.md
```

### File Description

| File                   | Description                  |
| ---------------------- | ---------------------------- |
| `inventory_manager.py` | Main Python application      |
| `inventory.csv`        | Stores inventory information |
| `sales_log.csv`        | Stores sales records         |
| `README.md`            | Project documentation        |

The program uses `inventory.csv` and `sales_log.csv` for storing inventory and sales information.

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/inventory-management-system.git
```

### 2. Install Required Libraries

```bash
pip install pandas numpy
```

### 3. Run the Application

```bash
python inventory_manager.py
```

## 💡 Technologies & Concepts

This project demonstrates:

* Python Functions
* Pandas DataFrames
* NumPy Arrays
* CSV File Handling
* File Operations
* Data Searching
* Data Filtering
* Sales Tracking
* Inventory Calculations
* Menu-driven Programming

## 🎯 Project Objective

The main objective of this project is to create a simple inventory management solution that helps track stock, manage sales, monitor low-stock products, and generate useful business information through a command-line interface.

## 👩‍💻 Author

**Roja M**

