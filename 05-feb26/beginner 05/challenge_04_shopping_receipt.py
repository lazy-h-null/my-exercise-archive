item1_name = input("Enter item 1 name: ")
item1_price = float(input(f"Enter price of {item1_name}: "))

item2_name = input("Enter item 2 name: ")
item2_price = float(input(f"Enter price of {item2_name}: "))

item3_name = input("Enter item 3 name: ")
item3_price = float(input(f"Enter price of {item3_name}: "))

total = item1_price + item2_price + item3_price

print("\n---------------------")
print(f" {item1_name:<10} ${item1_price:>6.2f}")
print(f" {item2_name:<10} ${item2_price:>6.2f}")
print(f" {item3_name:<10} ${item3_price:>6.2f}")
print("---------------------")
print(f" TOTAL          ${total:>6.2f}")