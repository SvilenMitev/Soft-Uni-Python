
bakary_dict = {}
while True:
    current_input = input()
    if current_input == "statistics":
        break
    list_input = current_input.split(": ")
    if list_input[0] not in bakary_dict:
        bakary_dict[list_input[0]] = int(list_input[1])
    else:
        bakary_dict[list_input[0]] += int(list_input[1])
print("Products in stock:")
for products, quantity in bakary_dict.items():
    print(f"- {products}: {quantity}")

print(f"Total Products: {len(bakary_dict.keys())}")
print(f"Total Quantity: {sum(bakary_dict.values())}")
