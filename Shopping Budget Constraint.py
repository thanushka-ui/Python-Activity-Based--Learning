budget = float(input("Enter budget: "))
n = int(input("Number of products: "))

total = 0

for i in range(n):
    price = float(input("Product price: "))
    quantity = int(input("Quantity: "))
    total += price * quantity

print("Total shopping cost =", total)

if total <= budget:
    print("Shopping is within budget")
else:
    print("Over budget by =", total - budget)