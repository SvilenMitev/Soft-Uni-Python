def order(product, number):
    if product == 'coffee':
        return number * 1.5
    elif product == 'coke':
        return number * 1.4
    elif product == 'water':
        return number * 1.0
    elif product == 'snacks':
        return number * 2.0


product_name = input()
number_of_products = int(input())
print("{:.2f}".format(order(product_name, number_of_products)))

