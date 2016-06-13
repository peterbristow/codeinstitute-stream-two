import unittest
from vending_machine_2 import *


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_get_choice(self):
        give_item_and_change('apple', '4')

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', '1.00 .50')
        self.assertIsNone(item)
        self.assertEqual(change, 1.35)

    def test_not_enough_change(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('apple', '.2')
        self.assertIsNone(item)
        self.assertEqual(change, 0.2)

    def test_lots_of_coins_given(self):
        """if user gives a lot of coins, they should not be given the correct change"""
        item, change, _ = give_item_and_change('apple', '1.00 0.5 0.2 0.1 0.1 0.05 0.02 0.02 0.01')
        self.assertEqual(item, 'apple')
        self.assertEqual(change, [1.0, 0.5, 0.05, 0.02])
