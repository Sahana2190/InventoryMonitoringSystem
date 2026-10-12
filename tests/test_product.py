
import unittest

from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.laptop = Product(
            "P101",
            "Laptop",
            "Electronics",
            8,
            10,
            45000
        )

    def test_inventory_value(self):
        self.assertEqual(self.laptop.inventory_value, 360000)

    def test_low_stock_status(self):
        self.assertEqual(self.laptop.stock_status, "LOW_STOCK")

    def test_reorder_quantity(self):
        self.assertEqual(self.laptop.reorder_quantity, 2)

    def test_out_of_stock_status(self):
        monitor = Product(
            "P104", "Monitor", "Electronics", 0, 5, 12000
        )
        self.assertEqual(monitor.stock_status, "OUT_OF_STOCK")

    def test_normal_stock_status(self):
        mouse = Product(
            "P102", "Mouse", "Accessories", 35, 15, 500
        )
        self.assertEqual(mouse.stock_status, "NORMAL")


if __name__ == "__main__":
    unittest.main()
