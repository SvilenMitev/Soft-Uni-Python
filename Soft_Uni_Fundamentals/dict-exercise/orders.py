product_dict = {}

while True:
    current_product_input = input().split()
    if 'buy' == current_product_input:
        break
    product = current_product_input[0]
    price = float(current_product_input[1])
    quantity = int(current_product_input[2])
    if product not in product_dict:
        product_dict[product] = [price, quantity]
    else:
        product_dict[product][0] = price
        product_dict[product][1] += quantity

print(product_dict)