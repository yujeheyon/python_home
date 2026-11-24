price = 12000
quantity = 3
discount_rate = 0.1
product = "노트"
is_member = True
subtotal = price * quantity
print(product, subtotal)
print(type(price).__name__, type(discount_rate).__name__)
print(subtotal >= 30000, is_member)
print(7 / 2, 7 // 2, 7 % 2)