import unittest
from utils.logic import calculate_minimum_delivery_cost

class TestDeliveryCost(unittest.TestCase):

    def test_case_1(self):
        order = {"A": 1, "G": 1, "H": 1, "I": 3}
        self.assertEqual(calculate_minimum_delivery_cost(order), 86)

    def test_case_2(self):
        order = {"A": 1, "B": 1, "C": 1, "G": 1, "H": 1, "I": 1}
        self.assertEqual(calculate_minimum_delivery_cost(order), 118)

    def test_case_3(self):
        order = {"A": 1, "B": 1, "C": 1}
        self.assertEqual(calculate_minimum_delivery_cost(order), 78)

    def test_case_4(self):
        order = {"A": 1, "B": 1, "C": 1, "D": 1}
        self.assertEqual(calculate_minimum_delivery_cost(order), 168)

if __name__ == '__main__':
    unittest.main()
