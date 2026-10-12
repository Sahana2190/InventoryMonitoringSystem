# 📦 Inventory Monitoring System

A Python-based inventory monitoring application that tracks product stock, identifies low-stock and out-of-stock items, calculates inventory value, and generates reports for inventory analysis.

## 📌 Project Overview

The Inventory Monitoring System is a collaborative Python project designed to simplify inventory tracking and stock monitoring. It processes inventory data from CSV files, validates input data, identifies products requiring restocking, generates category-wise reports, and records application activity through logging.

The project demonstrates practical implementation of Python programming, object-oriented concepts, data processing, exception handling, reporting, and automated unit testing.

## ✨ Features

- **Inventory Tracking:** Loads and processes product inventory data from CSV files.
- **Stock Status Monitoring:** Classifies products as `NORMAL`, `LOW_STOCK`, or `OUT_OF_STOCK`.
- **Low-Stock Alerts:** Identifies products whose quantities have reached or fallen below their reorder levels.
- **Out-of-Stock Detection:** Identifies products with zero available quantity.
- **Inventory Valuation:** Calculates the total value of available inventory.
- **Category-Wise Analysis:** Groups inventory data by product category.
- **Input Validation:** Checks required columns, missing values, duplicate product IDs, and invalid numeric values.
- **Automated Report Generation:** Generates inventory summary, low-stock, and category reports in CSV format.
- **Application Logging:** Records application events and errors.
- **Unit Testing:** Includes automated tests for product logic, inventory calculations, and file handling.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Pandas | Data processing and CSV handling |
| CSV | Inventory data storage and report generation |
| `unittest` | Automated testing |
| Git | Version control |
| GitHub | Source code hosting and collaboration |

## 📂 Project Structure

```text
InventoryMonitoringSystem_Sahana_Amrutha/
│
├── app.py
├── main.py
├── product.py
├── inventory_manager.py
├── file_handler.py
├── report_generator.py
├── logger_config.py
├── __init__.py
├── inventory.csv
├── requirements.txt
├── README.md
├── .gitignore
├── team_list.txt
│
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_inventory.py
│   └── test_file_handler.py
│
└── reports/                   # Generated at runtime
    ├── inventory_summary.csv
    ├── low_stock_report.csv
    └── category_report.csv
```

*Note: The `reports/` directory and `application.log` are excluded from version control through `.gitignore`.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Git
- Visual Studio Code or another Python-compatible editor

### 1. Clone the repository

```bash
git clone https://github.com/Sahana2190/InventoryMonitoringSystem.git
```

### 2. Navigate to the project directory

```bash
cd InventoryMonitoringSystem
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Running the Application

Run the following command from the project directory:

```bash
python app.py
```

The application displays an inventory summary and stock alerts, then generates reports in the `reports/` directory.

## 📊 Sample Execution Results

The current sample inventory produces the following results:

| Metric | Result |
|---|---:|
| Total Products | 5 |
| Total Units | 59 |
| Total Inventory Value | ₹4,54,300.00 |
| Low-Stock Products | 2 |
| Out-of-Stock Products | 1 |

### Sample Stock Alerts

```text
LOW STOCK: Laptop | Quantity: 8 | Reorder: 2
LOW STOCK: Keyboard | Quantity: 4 | Reorder: 6
OUT OF STOCK: Monitor | Reorder: 5
```

*Results are based on the sample inventory data included with the project.*

## 📑 Generated Reports

The application generates the following CSV reports:

| Report | Description |
|---|---|
| `inventory_summary.csv` | Provides an overall inventory summary |
| `low_stock_report.csv` | Lists products requiring stock attention |
| `category_report.csv` | Summarizes inventory by category |

Application events and errors are recorded in `application.log`.

## 🧪 Running Unit Tests

Execute the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

**Current test results:** 16 tests passed.

### Areas Covered by Tests

- Product inventory value calculations
- Normal, low-stock, and out-of-stock status
- Reorder quantity calculations
- Total product and unit counts
- Total inventory valuation
- Low-stock and out-of-stock identification
- Category grouping
- CSV loading and validation
- Missing files and required columns
- Duplicate product IDs and negative quantities

## 🧠 Python Concepts Demonstrated

- Classes, functions, and modules
- Object-oriented programming and data classes
- File handling and data processing with Pandas
- Input validation and exception handling
- Application logging
- Report generation
- Automated unit testing
- Git version control and GitHub collaboration

## 🚀 Future Enhancements

Potential improvements include:

- Interactive inventory dashboard
- Database integration for persistent storage
- Configurable reorder thresholds
- Email notifications for critical stock levels
- Inventory history and trend analysis

## 👥 Project Team

This project was collaboratively developed by:

- **Sahana H.**
- **Amrutha S**

### Project Details

- **Project:** Inventory Monitoring System
- **Domain:** Python Application Development
- **Version Control:** Git and GitHub

---

*Developed collaboratively to demonstrate inventory tracking, stock monitoring, data validation, reporting, logging, and software testing using Python.*