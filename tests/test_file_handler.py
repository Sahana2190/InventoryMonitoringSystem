
import unittest
import tempfile
from pathlib import Path

import pandas as pd

from file_handler import load_inventory


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.csv_path = Path(self.temp_dir.name) / "inventory.csv"

        pd.DataFrame({
            "product_id": ["P101", "P102"],
            "name": ["Laptop", "Mouse"],
            "category": ["Electronics", "Accessories"],
            "quantity": [8, 35],
            "reorder_level": [10, 15],
            "unit_price": [45000, 500],
        }).to_csv(self.csv_path, index=False)

    def test_load_valid_csv(self):
        df = load_inventory(self.csv_path)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.loc[0, "name"], "Laptop")

    def test_missing_file(self):
        missing = Path(self.temp_dir.name) / "missing.csv"
        with self.assertRaises(FileNotFoundError):
            load_inventory(missing)

    def test_negative_quantity(self):
        df = pd.read_csv(self.csv_path)
        df.loc[0, "quantity"] = -1
        df.to_csv(self.csv_path, index=False)

        with self.assertRaisesRegex(ValueError, "quantity cannot contain negative values"):
            load_inventory(self.csv_path)

    def test_missing_required_column(self):
        pd.DataFrame({
            "product_id": ["P101"],
            "name": ["Laptop"],
        }).to_csv(self.csv_path, index=False)

        with self.assertRaisesRegex(ValueError, "Missing columns"):
            load_inventory(self.csv_path)

    def test_duplicate_product_ids(self):
        df = pd.read_csv(self.csv_path)
        df.loc[1, "product_id"] = "P101"
        df.to_csv(self.csv_path, index=False)

        with self.assertRaisesRegex(ValueError, "Duplicate product IDs"):
            load_inventory(self.csv_path)


if __name__ == "__main__":
    unittest.main()
