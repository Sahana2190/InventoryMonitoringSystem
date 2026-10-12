
import unittest

from product import Product
from inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.products = [
            Product("P101", "Laptop", "Electronics", 8, 10, 45000),
            Product("P102", "Mouse", "Accessories", 35, 15, 500),
            Product("P103", "Keyboard", "Accessories", 4, 10, 1200),
            Product("P104", "Monitor", "Electronics", 0, 5, 12000),
            Product("P105", "Office Chair", "Furniture", 12, 5, 6000),
        ]
        self.inventory = InventoryManager(self.products)

    def test_total_products(self):
        self.assertEqual(self.inventory.total_products(), 5)

    def test_total_units(self):
        self.assertEqual(self.inventory.total_units(), 59)

    def test_total_inventory_value(self):
        self.assertEqual(self.inventory.total_inventory_value(), 454300)

    def test_low_stock_products(self):
        names = [p.name for p in self.inventory.low_stock_products()]
        self.assertEqual(names, ["Laptop", "Keyboard"])

    def test_out_of_stock_products(self):
        names = [p.name for p in self.inventory.out_of_stock_products()]
        self.assertEqual(names, ["Monitor"])

    def test_group_by_category(self):
        groups = self.inventory.group_by_category()
        self.assertEqual(
            sorted(groups.keys()),
            ["Accessories", "Electronics", "Furniture"]
        )
        self.assertEqual(len(groups["Electronics"]), 2)
        self.assertEqual(len(groups["Accessories"]), 2)
        self.assertEqual(len(groups["Furniture"]), 1)


if __name__ == "__main__":
    unittest.main()
