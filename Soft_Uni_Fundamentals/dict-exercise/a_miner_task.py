temp_list = []

while True:
    current_input = input()
    if current_input == "stop":
        break
    temp_list.append(current_input)

miner_dict = {}

for i in range (0, len(temp_list), 2 ):
    resource = temp_list[i]
    quantity = temp_list[i+1]
    if resource not in miner_dict:
        miner_dict[resource] = 0
    miner_dict[resource] += int(quantity)

for resource, quantity in miner_dict.items():
    print(f"{resource} -> {quantity}")

