def basket_total(*price):
    return sum(price)
print(basket_total(1000, 2000, 3000, 4000, 5000))

products = [("pen", 1500), ("book", 15000), ("cup", 8000), ("clock", 12000), ("note", 4000)]
print(sorted(products, key = lambda item : len(item[0])))
print(sorted(products, key = lambda item : item[1], reverse = True))