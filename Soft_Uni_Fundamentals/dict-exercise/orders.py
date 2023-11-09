product_dict = {}

while True:
    current_product_input = input().split()
    if ['buy'] == current_product_input:
        break
    product = current_product_input[0]
    price = float(current_product_input[1])
    quantity = int(current_product_input[2])
    if product not in product_dict:
        product_dict[product] = [price, quantity]
    else:
        product_dict[product][0] = price
        product_dict[product][1] += quantity

final_dict = {}
for keys, values in product_dict.items():
    final_dict[keys] = values[0] * values[1]

for keys, values in final_dict.items():
    print(f"{keys} -> {values:.2f}")
