import unittest

class Tests(unittest.TestCase):
    
    def test_single_item_no_taxes_or_shipping_fees(self, item, location):
        total_cost = calculate_total_cost(item, location)
        self.assertEqual(total_cost, 1)
    
    def test_multiple_items_no_taxes_or_shipping_fees(self, items, location):

        total_cost = calculate_total_cost(items, location)
        self.assertEqual(total_cost, 2)
    
    def test_calculate_taxes(self, items, location):
        taxes = calculate_taxes(items, location)
        self.assertEqual(taxes, 1)
    
    def test_calculate_shipping_fees(self, items, location):
        total_weight = calculate_total_weight(items)
        shipping_fees = calculate_shipping_fees(location, total_weight)
        self.assertEqual(shipping_fees, 10)
    
    def test_total_cost_with_taxes_and_shipping_fees(self, items, location):
        total_cost = calculate_total_cost(items, location)
        self.assertEqual(total_cost, 30)

if __name__ == '__main__':
    unittest.main()
