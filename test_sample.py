def test_single_item_no_tax_or_shipping():
    items = [("apple", 1, 0.50)]
    location = "NY"
    assert calculate_total(items, location) == 0.50


def calculate_total(items, location):
    total_cost = 0
    for item in items:
        total_cost += item[1] * item[2]
    return total_cost
