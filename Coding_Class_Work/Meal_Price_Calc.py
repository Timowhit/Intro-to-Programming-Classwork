print()
print(f"What is the price of a child's meal? ")
child_price = input(f"Child's Meal: $")

print()
print(f"What is the price of an adult's meal? ")
adult_price = input(f"Adult's Meal: $")

print()
print(f"How many children are there? ")
child_count = input(f"How many children? ")

print()
print(f"How many adults are there? ")
adult_count = input(f"How many adults? ")


print("-----------------")
print()
print(f"Subtotal: ${int(child_price) * int(child_count) + int(adult_price) * int(adult_count)} ")

print()
print(f"What is the sales tax? ")
sales_tax = input(f"Sales Tax: ");print("%")

subtotal = ((int(child_price) * int(child_count) + int(adult_price) * int(adult_count)))
print()
sales_tax2 = subtotal * (int(sales_tax)/100)
print(f"Sales tax: $ {round(int(sales_tax2), 2)}")

final_total = subtotal * (int(sales_tax)/100 + 1)
print()
print(f"Your total is ${final_total}")