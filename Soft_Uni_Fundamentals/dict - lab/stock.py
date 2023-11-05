initial_input = input().split()
in_stock_dict = {}
for i in range(0, len(initial_input), 2):
    key = initial_input[i]
    value = initial_input[i+1]
    in_stock_dict[key] = int(value)

requested_input = input().split()
for product in requested_input:
    if product in in_stock_dict:
        print(f"We have {in_stock_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
