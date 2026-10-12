# Inventory Monitoring System

A Python application that loads inventory data, validates input, calculates inventory values, identifies low/out-of-stock products, and generates CSV reports.

## Project structure

- `__init__.py` — marks the project directory as a Python package.
- `app.py` — application entry point.
- `main.py` — main application workflow.
- `product.py` — product model and stock status logic.
- `inventory_manager.py` — inventory calculations and filters.
- `file_handler.py` — CSV/XLSX loading and validation.
- `report_generator.py` — report generation.
- `logger_config.py` — logging setup.
- `inventory.csv` — sample input data.
- `tests/` — test files.

## Setup

1. Install Python 3.10 or later.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run the application from this folder: `python app.py`
4. Run the existing test scripts from this folder: `python -m tests.test_product`, `python -m tests.test_inventory`, and `python -m tests.test_file_handler`. These files are script-based checks, not `unittest.TestCase` tests.

The application creates a `reports/` folder when it successfully generates reports. Runtime logs are local and are not included in this package.
