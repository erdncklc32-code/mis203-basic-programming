
def calculate_subtotal(prices):
    return sum(prices)


def get_discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    return 0.0


def calculate_shipping(subtotal):
    if subtotal >= 150:
        return 0
    return 15


def calculate_total(prices):
    subtotal = calculate_subtotal(prices)
    discount_rate = get_discount_rate(subtotal)
    discount = subtotal * discount_rate
    shipping = calculate_shipping(subtotal)
    return subtotal - discount + shipping


# Test cases
assert calculate_subtotal([40, 60]) == 100
assert get_discount_rate(99.99) == 0.0
assert get_discount_rate(100) == 0.10
assert calculate_shipping(150) == 0
assert calculate_total([40, 60]) == 105
assert calculate_total([100, 50]) == 135

# Sample order 1
order1 = [40, 60]
print("Order 1 total:", calculate_total(order1))

# Sample order 2
order2 = [100, 50]
print("Order 2 total:", calculate_total(order2))
