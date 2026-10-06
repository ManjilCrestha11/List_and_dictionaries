product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

print("Name:", product["name"])
print("Brand:", product["brand"])
print("Price:", product["price"])
print("Quantity:", product["quantity"])

total = product["price"] * product["quantity"]
print("Total value:", total)

product["quantity"] -= 2

print("Quantity after selling 2:", product["quantity"])